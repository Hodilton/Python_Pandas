class GraphConfig:
    """
    #: ID for each pokemon
    Name:      Name of each pokemon
    Type 1:    Each pokemon has a type, this determines weakness/resistance to attacks
    Type 2:    Some pokemon are dual type and have 2
    Total:     sum of all stats that come after this, a general guide to how strong a pokemon is
    HP:        hit points, or health, defines how much damage a pokemon can withstand before fainting
    Attack:    the base modifier for normal attacks (eg. Scratch, Punch)
    Defense:   the base damage resistance against normal attacks
    SP Atk:    special attack, the base modifier for special attacks (e.g. fire blast, bubble beam)
    SP Def:    the base damage resistance against special attacks
    Speed:     determines which pokemon attacks first each round
    """
    @staticmethod
    def get_graph_config():
        hp_distribution = {
            "type": "box",
            "x": "Type 1",
            "y": "HP",
            "title": "Distribution of Hit Points (HP) among Pokémon",
            "color": "Type 1"
        }

        total_vs_speed = {
            "type": "scatter",
            "x": "Total",
            "y": "Speed",
            "title": "Total vs Speed for Pokémon",
            "color": "Type 1"
        }

        attack_preference = {
            "type": "histogram",
            "x": ["Attack", "Sp. Atk"],
            "barmode": "group",
            "title": "Comparison of Attack Types among Pokémon Types"
        }

        type_strength_distribution = {
            "type": "pie",
            "names": "Type 1",
            "values": "Total",
            "title": "Distribution of Pokémon Types by Strength (Total)"
        }

        attack_defense_relationship = {
            "type": "scatter_3d",
            "x": "Attack",
            "y": "Defense",
            "z": "Total",
            "color": "Type 1",
            "title": "The relationship between the Attack and Defense parameters for different types of Pokemon",
            "labels": {'Attack': 'Attack', 'Defense': 'Defense', 'Total': 'Total'}
        }

        return {
            "attack_defense_relationship": attack_defense_relationship,
            "type_strength_distribution": type_strength_distribution,
            "attack_preference": attack_preference,
            "total_vs_speed": total_vs_speed,
            "hp_distribution": hp_distribution,
        }
