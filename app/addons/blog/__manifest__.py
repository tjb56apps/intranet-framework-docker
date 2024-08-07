{
    "id": "A001",
    "name": "Blog",
    "version": "1.0.1",
    "path": "blog",
    "nav": [
        {
            "id": "0",
            "type": "single",
            "icon": "fa-home",
            "name": "Home",
            "path": "",
            "leveling": ["parent", "member"]
        },
        {
            "id": "1",
            "type": "dropdown",
            "icon": "fa-file-word-o",
            "name": "Content",
            "leveling": ["parent", "member"],
            "child": [
                {
                    "name": "New Post",
                    "icon": "fa-circle-o",
                    "path": "create-post",
                    "leveling": ["parent"]
                },
                {
                    "name": "New Page",
                    "icon": "fa-circle-o",
                    "path": "create-page",
                    "leveling": ["parent", "member"]
                }
            ]
        },
        {
            "id": "2",
            "type": "dropdown",
            "icon": "fa-user",
            "name": "Administrator",
            "leveling": ["parent", "member"],
            "child": [
                {
                    "name": "Users",
                    "icon": "fa-circle-o",
                    "path": "users",
                    "leveling": ["parent", "member"]
                },
                {
                    "name": "Setting",
                    "icon": "fa-circle-o",
                    "path": "setting",
                    "leveling": ["parent"]
                }
            ]
        }
    ]
}