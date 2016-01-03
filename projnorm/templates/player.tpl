"player": {
    "ids": {
        {% for key in id_systems %}
            "key_{{ key }}": null{% if not loop.last %},{% endif %}
        {% endfor %}
    },
    "team_name": null,
    "league": null,
    "roles": null,
    "name_last": null,
    "name_first": null,
    "name_full": null,
    "name_lcf": null,
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
