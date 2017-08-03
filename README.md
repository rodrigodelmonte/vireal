# Code Challenge.

## Run app.
**You need docker installed on your machine.**
```sh
$ docker run -p 5000:5000 rodrigodelmonte/vireal
```

## Test app.
```sh
$ cd app
$ python run_tests.py
```

## Use the app.

### Create a propertie:
* Resquast example:
```sh
curl -H "Content-Type: application/json" -X POST -d '{ "title": "Imovel codigo 1, com 5 quartos e 4 banheiros", "price": 1250000, "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", "x": 870, "y": 867, "beds": 5, "baths": 4, "squareMeters": 134 }' http://localhost:5000/properties
```
* Response example:
```sh
{
  "message": "Propertie success created! Id: 6713"
}

```

### To looking for a specific propertie:
* Resquast example:
```sh
$ curl http://localhost:5000/properties/10
```
* Response example:
```sh
{
  "baths": 2,
  "beds": 3,
  "description": "In reprehenderit sit dolor nostrud enim nisi proident non deserunt incididunt pariatur sunt. Adipisicing nisi fugiat commodo cillum ea aute anim magna eu magna duis officia.",
  "id": 10,
  "price": 661000,
  "province": "Scavy",
  "squareMeters": 64,
  "title": "Im\u00f3vel c\u00f3digo 10, com 3 quartos e 2 banheiros.",
  "x": 304,
  "y": 225
}
```
### To looking for properties from an specific area:
* Resquast example:
```sh
$ curl -X GET "http://localhost:5000/properties?ax=200&ay=1000&bx=300&by=1000"
```
* Response example:
```sh
{
    "foundProperties": 1006,
    "properties": [
        {
            "baths": 1,
            "beds": 2,
            "description": "Incididunt dolor ad proident incididunt culpa nostrud ea deserunt dolor. Tempor eiusmod elit esse adipisicing reprehenderit eiusmod mollit ex velit sunt dolor sunt.",
            "id": 5,
            "price": 560000,
            "province": "Gode",
            "squareMeters": 54,
            "title": "Imóvel código 5, com 2 quartos e 1 banheiros.",
            "x": 34,
            "y": 660
        },
        {
            "baths": 4,
            "beds": 5,
            "description": "Enim amet Lorem exercitation consectetur sunt nulla incididunt aliqua nisi do voluptate laborum. Est mollit consectetur qui velit consequat reprehenderit et adipisicing occaecat labore labore ipsum do aliquip.",
            "id": 7,
            "price": 1354000,
            "province": "Gode",
            "squareMeters": 131,
            "title": "Imóvel código 7, com 5 quartos e 4 banheiros.",
            "x": 38,
            "y": 664
        },
        {
            "baths": 4,
            "beds": 5,
            "description": "Ullamco non dolore commodo laboris excepteur officia laboris id duis do velit ullamco esse mollit. Ex sunt enim fugiat culpa mollit cupidatat do laboris magna ut proident id quis.",
            "id": 52,
            "price": 1641000,
            "province": "Scavy",
            "squareMeters": 163,
            "title": "Imóvel código 52, com 5 quartos e 4 banheiros.",
            "x": 8,
            "y": 162
        },
        ...
```