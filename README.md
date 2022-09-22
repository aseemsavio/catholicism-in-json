# catholicism-in-json

This repository houses the following resources, all in usable JSON format.

1. __Catechism of the Catholic Church__
2. __The Canon Law__
3. __General Instruction of The Roman Missal__

This repo utilises pickles from the
very well-known Catholic Reddit bot [/u/Catebot](https://www.reddit.com/user/Catebot/) to create the JSONs. Please refer
the [Catebot's GitHub repo](https://github.com/konohitowa/catebot) for more information.

The JSON files will be released in the releases section shortly.

## Structure of the JSON files

1. `canon.json`

The following is a snippet from the `canon.json` file.
At the top level is an array, which houses all the Canon laws.
Each law has a `law_id`, and either `law_text` or an array of `sub_laws`.
The `sub_laws` themselves have a `sub_law_id` and a `sub_law_text`.

```json
[
  {
    "law_id": 4,
    "law_text": "Acquired rights and privileges granted to physical or juridic persons up to this time by the Apostolic See remain intact if they are in use and have not been revoked, unless the canons of this Code expressly revoke them.\n\n"
  },
  {
    "law_id": 5,
    "sub_laws": [
      {
        "sub_law_id": 1,
        "sub_law_text": "Universal or particular customs presently in force which are contrary to the prescripts of these canons and are reprobated by the canons of this Code are absolutely suppressed and are not permitted to revive in the future. Other contrary customs are also considered suppressed unless the Code expressly provides otherwise or unless they are centenary or immemorial customs which can be tolerated if, in the judgment of the ordinary, they cannot be removed due to the circumstances of places and persons.\n\n"
      },
      {
        "sub_law_id": 2,
        "sub_law_text": "Universal or particular customs beyond the law (*praeter ius*) which are in force until now are preserved.\n\n"
      }
    ]
  }
]
```
