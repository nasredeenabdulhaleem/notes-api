# Notes API

## Setting up the Project

### Install Dependencies

1. **Python 3.9** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Django](http://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

- [Django Rest Framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

- [django-cors-headers](https://pypi.org/project/django-cors-headers/) is a Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).

### Set up the Database

With Postgres running, create a `Notes` database:

```bash
createdb Notes
```

### Set up the Project

Start a terminal and Navigate to the Api directory to create a virtual environment.

`python -m venv env`

From your home directory activate your virtual environment:

`\env\Scripts\activate`

Run the following code to install the project dependencies

` pip install -r requirements.txt`

### Running the Server

From within the `./Api` directory first ensure you are working using your created virtual environment.

To run the server, execute:

`python manage.py runserver`

The server will start on localhost on port 8000 but to run it on a different port you can append a different port to the comand.

## To Do Tasks

These is the files you'd want to edit in the backend

1. `Api/notes/settings.py`

Navigate to `line 80` and change the settings to your preffered database configuration.

### Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The api is hosted at the default, `http://127.0.0.1:8000/`, which is set as a proxy in the frontend configuration.
- Authentication: This version of the application requires authentication and API Token for subsequent requests.

### Error Handling

Errors are returned as JSON objects in the following format:

```json
{
	"detail": "Not found."
}
```

The API will return three error types when requests fail:

- 401: Unauthorized
- 400: Bad Request
- 404: Not Found
- 422: Not Processable

## Endpoints

#### GET /api/

- General:
  - Request parameters (optional): page:int
  - Returns a list of all notes
  - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
- Sample: `curl http://127.0.0.1:8000/api/`

```json
{
	"count": 5,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"title": "First Note",
			"note": "new note one"
		},
		{
			"id": 2,
			"title": "Second Note",
			"note": "new note two"
		},
		{
			"id": 3,
			"title": "Third Note",
			"note": "new note three"
		},
		{
			"id": 15,
			"title": "Fourth Four",
			"note": "new note four"
		},
		{
			"id": 16,
			"title": "Fifth Note",
			"note": "new note fifth"
		}
	]
}
```

#### GET /api/{int}/

- Fetches a dictionary of a note detail
- Request Arguments: one "Note ID"
- Returns: Two objects with

  `id: id_int`

  `title: title_string`

  `note: note_string`

  key: value pairs.

```json
{
	"id": 1,
	"title": "First Note",
	"note": "new note one"
}
```

#### POST /api/create/

- POST a dictionary of a note detail
- Request Arguments: None
- Sample: `curl -X POST http://127.0.0.1:8000/api/ -d {{"title":"note 3","note":"note 3"}}`
- Returns: dictionary of objects

  `id: id_int`

  `title: title_string`

  `note: note_string`

  key: value pairs.

```json
{
	"count": 5,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"title": "First Note",
			"note": "new note one"
		},
		{
			"id": 2,
			"title": "Second Note",
			"note": "new note two"
		},
		{
			"id": 3,
			"title": "Third Note",
			"note": "new note three"
		},
		{
			"id": 15,
			"title": "Fourth Four",
			"note": "new note four"
		},
		{
			"id": 17,
			"title": "note 3",
			"note": "new note"
		}
	]
}
```

#### PATCH PUT /api/int/update

- PUT a dictionary of a note
- Request Arguments:
- Sample: `curl -X Patch http://127.0.0.1:8000/api/{int}/update -d {{"title":"note 3","note":"note 3"}}`
- Returns: dictionary of objects

  `id: id_int`

  `title: title_string`

  `note: note_string`

  key: value pairs.

  ```json
  {
  	"id": 4,
  	"title": "second user note",
  	"note": "blu bla 4"
  }
  ```

#### GET api//search/

- General:

- Request body: searchTerm
  -Searches through the Notes in the database for the given keywords. returns a list of all available Note title which has the keyword, success value, and total number of notes gotten from the search. -`curl -X GET http://127.0.0.1:8000/api/search -H "Content-Type: application/json" -d "query=second%20user"

```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 4,
            "title": "second user note",
            "note": "blu bla 4"
        }

    ]
}
```

#### DELETE /api/{note_id}/delete/

- General:
  - request arguments: note_id:int
  - Deletes the note of the given ID if it exists. Returns success value
- `curl -X DELETE http://127.0.0.1:8000/api/id/delete?page=1`

```
{
  "Note": [
        {
            "id": 4,
            "title": "second user note",
            "note": "blu bla 4"
        }
  ],
  "deleted": 5,
  "success": true,
}
```

## Authors

Yours truly, Nasredeen Abdulhaleem
