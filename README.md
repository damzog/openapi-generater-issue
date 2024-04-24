# openapi-generater-issue

Simple example to demonstrate an issue with openapi generator for python. Keep an eye on the relations attribute which is a dict:

```pyton
...
class User(BaseModel):
    name: str = None
    address: Address = None
    relations: Dict[str, Address] = None
...
```
Translates into following schema using fastapi openapi json schema generator:

```json
      "User": {
        "properties": {
          "name": {
            "type": "string",
            "title": "Name"
          },
          "age": {
            "type": "integer",
            "title": "Age"
          },
          "relations": {
            "additionalProperties": {
              "$ref": "#/components/schemas/Address"
            },
            "type": "object",
            "title": "Relations"
          }
        },
        "type": "object",
        "title": "User"
      }
```
Which I think is fine according to [Openapi spec](https://swagger.io/docs/specification/data-models/dictionaries/)

But the generated code fails to deserialize an example 
    
```python
@app.get("/")
async def root() -> User:
    return {"name": "John", "age": 25, "relations": {"friend": {"street": "123 Main St", "city": "Springfield"},
                                                     "family": {"street": "456 Elm St", "city": "Springfield"}}}
```
results in
```
 /home/dzj8fe/ws/fastapi-test/.venv/bin/python /home/dzj8fe/ws/fastapi-test/client.py 
The response of DefaultApi->root_get:

'{"name":"John", "age": 25}'

Process finished with exit code 0  
```
The reason is probably the "not" in the the generated deserilization code:

```python
    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of User from a dict"""
        if obj is None:
            return None
        # Why don't we just let handle pydantic the deserialization? The generated code completely ignores the relations 
        # attribute.
        # 
        # This code works for me
        #  _obj = cls.model_validate(obj)
        # return _obj
        # 
        # The generated code below does not
        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "address": Address.from_dict(obj.get("address")) if obj.get("address") is not None else None,
        })
        return _obj
```