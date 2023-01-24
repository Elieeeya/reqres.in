from pytest_voluptuous import S

list_user = S({
    "page": int,
    "per_page": int,
    "total": int,
    "total_pages": int,
    "data": [{
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        },
    ],
    "support":
    {
        "url": str,
        "text": str
    }
})


single_user = S({
    "data": {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    "support": {
        "url": str,
        "text": str
    }
})


list_resource = S({
    "page": int,
    "per_page": int,
    "total": int,
    "total_pages": int,
    "data": [{
            "id": int,
            "name": str,
            "year": int,
            "color": str,
            "pantone_value": str
        },
    ],
    "support":
    {
        "url": str,
        "text": str
    }
})

single_resource = S({
    "data": {
        "id": int,
        "name": str,
        "year": int,
        "color": str,
        "pantone_value": str
        },
    "support":
    {
        "url": str,
        "text": str
    }
})