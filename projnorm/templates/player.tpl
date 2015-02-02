"player": {
    "ids": {
        {% for key in id_systems %}
            "key_{{ key }}": null{% if not loop.last %},{% endif %}
        {% endfor %}
    },
    "team_name": null,
    "league": null,
    "roles": null,
    "name": {
        "first": null,
        "last": null,
        "full": null
    },
    "age": null,
    "hands": {
        "bats": null,
        "throws": null
    }
},

"components": {
    {%- for component in components %}
        "{{ component }}": null{% if not loop.last %},{% endif %}
    {%- endfor %}
}
