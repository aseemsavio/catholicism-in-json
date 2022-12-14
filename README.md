# ⛪️ catholicism-in-json

This repository houses the following resources, all in usable JSON format.

1. 📒 __Catechism of the Catholic Church__
2. 🇻🇦 __The Canon Law__
3. ⛪️ __General Instruction of The Roman Missal__

This repo utilizes pickles from the
well-known Catholic Reddit bot [/u/Catebot](https://www.reddit.com/user/Catebot/) to create the JSON files. Please refer
to the [Catebot's GitHub repo](https://github.com/konohitowa/catebot) for more information.
You can access the JSON files for your use from
the [releases](https://github.com/aseemsavio/catholicism-in-json/releases) section.
Note that the text in these files is in `markdown` style - with bold, italics, quotes, etc.

## Structure of the JSON files

1. `catechism.json`

This file is straightforward. It is a JSON list consisting of all the paragraphs of the Catechism of The Church.

```json
[
  {
    "id": 1,
    "text": "God, infinitely perfect and blessed in himself, in a plan of sheer goodness freely created man to make him share in his own blessed life. For this reason, at every time and in every place, God draws close to man. He calls man to seek him, to know him, to love him with all his strength. He calls together all men, scattered and divided by sin, into the unity of his family, the Church. To accomplish this, when the fullness of time had come, God sent his Son as Redeemer and Savior. In his Son and through him, he invites men to become, in the Holy Spirit, his adopted children and thus heirs of his blessed life.\n"
  },
  {
    "id": 2,
    "text": "So that this call should resound throughout the world, Christ sent forth the apostles he had chosen, commissioning them to proclaim the gospel: \"Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit, teaching them to observe all that I have commanded you; and lo, I am with you always, to the close of the age.\" Strengthened by this mission, the apostles \"went forth and preached everywhere, while the Lord worked with them and confirmed the message by the signs that attended it.\"\n"
  }
]
```

2. `canon.json`

The following is a snippet from the `canon.json` file.
At the top level is an array, which houses all the Canon laws.
Each law has an `id` and either a `text` or an array - `sections`.
Each `sections` object contains an `id` and a `text`.

```json
[
  {
    "id": 4,
    "text": "Acquired rights and privileges granted to physical or juridic persons up to this time by the Apostolic See remain intact if they are in use and have not been revoked, unless the canons of this Code expressly revoke them.\n\n"
  },
  {
    "id": 5,
    "sections": [
      {
        "id": 1,
        "text": "Universal or particular customs presently in force which are contrary to the prescripts of these canons and are reprobated by the canons of this Code are absolutely suppressed and are not permitted to revive in the future. Other contrary customs are also considered suppressed unless the Code expressly provides otherwise or unless they are centenary or immemorial customs which can be tolerated if, in the judgment of the ordinary, they cannot be removed due to the circumstances of places and persons.\n\n"
      },
      {
        "id": 2,
        "text": "Universal or particular customs beyond the law (*praeter ius*) which are in force until now are preserved.\n\n"
      }
    ]
  }
]
```

3. `girm.json`

The contents of The __General Instruction of The Roman Missal__ file look as follows.

```json
[
  {
    "id": 1,
    "text": "As Christ the Lord was about to celebrate with the disciples the paschal supper in which he instituted the Sacrifice of his Body and Blood, he commanded that a large, furnished upper room be prepared (Lk 22:12). Indeed, the Church has always judged that this command also applied to herself whenever she decided about things related to the disposition of people's minds, and of places, rites, and texts for the Celebration of the Most Holy Eucharist. The present norms, too, prescribed in keeping with the will of the Second Vatican Council, together with the new Missal with which the Church of the Roman Rite will henceforth celebrate the Mass, are again a demonstration of this same solicitude of the Church, of her faith and her unaltered love for the supreme mystery of the Eucharist, and also attest to her continuous and consistent tradition, even though certain new elements have been introduced.\n\n"
  }
]
```

## Note to Contributors/Developers

If you're feeling particularly nerdy, and hence wish to generate the JSON files by yourselves,
you may run the following command from the root of this project.
You need to have Python installed on your machine for this.

```
 python main.py
```

Feel free to leave me a note when you end up using the JSONs from this project.
It would be fun for me to learn how and where you put this project to use! 🤓

