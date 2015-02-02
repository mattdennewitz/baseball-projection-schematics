{
    "batting": {
        {% with components=config.components.batting %}
            {% include "player.tpl" with context %}
        {% endwith %}
    },

    "pitching": {
        {% with components=config.components.pitching %}
            {% include "player.tpl" with context %}
        {% endwith %}
    }
}
