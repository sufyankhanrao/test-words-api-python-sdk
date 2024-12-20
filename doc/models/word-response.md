
# Word Response

This custom type contains the response for word API.

## Structure

`WordResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `str` | Required | The word that is searched. |
| `results` | [`List[WordDetails]`](../../doc/models/word-details.md) | Required | This field contains detailed information of the word. |
| `pronunciation` | `object` | Optional | This model contains pronunciation details of a specific word. |
| `frequency` | `float` | Optional | The frequency of the word usage. |
| `syllables` | [`SyllableDetails`](../../doc/models/syllable-details.md) | Optional | This custom type contains the syllable details for word API. |

## Example (as JSON)

```json
{
  "word": "wind",
  "results": [
    {
      "definition": "raise or haul up with or as if with mechanical help",
      "partOfSpeech": "verb",
      "synonyms": [
        "hoist",
        "lift"
      ],
      "typeOf": [
        "raise",
        "lift",
        "get up",
        "elevate",
        "bring up"
      ],
      "hasTypes": [
        "trice up",
        "trice"
      ]
    },
    {
      "definition": "catch the scent of; get wind of",
      "partOfSpeech": "verb",
      "synonyms": [
        "nose",
        "scent"
      ],
      "typeOf": [
        "smell"
      ],
      "hasTypes": [
        "hasTypes4",
        "hasTypes3"
      ]
    },
    {
      "definition": "a reflex that expels intestinal gas through the anus",
      "partOfSpeech": "noun",
      "synonyms": [
        "breaking wind",
        "fart",
        "farting",
        "flatus"
      ],
      "typeOf": [
        "reflex",
        "instinctive reflex",
        "innate reflex",
        "reflex action",
        "physiological reaction",
        "unconditioned reflex",
        "inborn reflex",
        "reflex response"
      ],
      "hasTypes": [
        "hasTypes4",
        "hasTypes3"
      ]
    },
    {
      "definition": "form into a wreath",
      "partOfSpeech": "verb",
      "synonyms": [
        "wreathe"
      ],
      "typeOf": [
        "twine",
        "intertwine",
        "lace",
        "entwine",
        "enlace",
        "interlace"
      ],
      "hasTypes": [
        "hasTypes4",
        "hasTypes3"
      ]
    },
    {
      "definition": "empty rhetoric or insincere or exaggerated talk",
      "partOfSpeech": "noun",
      "synonyms": [
        "idle words",
        "jazz",
        "malarkey",
        "malarky",
        "nothingness"
      ],
      "typeOf": [
        "talking",
        "talk"
      ],
      "derivation": [
        "windy"
      ],
      "examples": [
        "that's a lot of wind"
      ],
      "hasTypes": [
        "hasTypes4",
        "hasTypes3"
      ]
    },
    {
      "definition": "arrange or or coil around",
      "partOfSpeech": "verb",
      "synonyms": [
        "roll",
        "twine",
        "wrap"
      ],
      "typeOf": [
        "displace",
        "move"
      ],
      "hasTypes": [
        "loop",
        "ball",
        "spool",
        "clew",
        "clue",
        "coil",
        "curl",
        "reel"
      ],
      "antonyms": [
        "unwind"
      ],
      "derivation": [
        "winder"
      ]
    },
    {
      "definition": "to move or cause to move in a sinuous, spiral, or circular course",
      "partOfSpeech": "verb",
      "synonyms": [
        "meander",
        "thread",
        "wander",
        "weave"
      ],
      "typeOf": [
        "go",
        "locomote",
        "move",
        "travel"
      ],
      "hasTypes": [
        "snake"
      ],
      "verbGroup": [
        "wander"
      ],
      "examples": [
        "the river winds through the hills"
      ]
    },
    {
      "definition": "extend in curves and turns",
      "partOfSpeech": "verb",
      "synonyms": [
        "curve",
        "twist"
      ],
      "typeOf": [
        "be"
      ],
      "hasTypes": [
        "circumvolute",
        "spiral",
        "snake"
      ],
      "examples": [
        "The road winds around the lake"
      ]
    },
    {
      "definition": "the act of winding or twisting",
      "partOfSpeech": "noun",
      "synonyms": [
        "twist",
        "winding"
      ],
      "typeOf": [
        "rotation",
        "rotary motion"
      ],
      "examples": [
        "he put the key in the old clock and gave it a good wind"
      ],
      "hasTypes": [
        "hasTypes4",
        "hasTypes3"
      ]
    },
    {
      "definition": "a musical instrument in which the sound is produced by an enclosed column of air that is moved by bellows or the human breath",
      "partOfSpeech": "noun",
      "synonyms": [
        "wind instrument"
      ],
      "typeOf": [
        "instrument",
        "musical instrument"
      ],
      "hasTypes": [
        "organ pipe",
        "whistle",
        "post horn",
        "brass",
        "pipe",
        "sweet potato",
        "pipe organ",
        "kazoo",
        "pipework",
        "free-reed instrument",
        "ocarina",
        "organ",
        "woodwind instrument",
        "brass instrument",
        "woodwind",
        "wood"
      ],
      "hasParts": [
        "mouthpiece",
        "bell",
        "embouchure"
      ]
    },
    {
      "definition": "air moving (sometimes with considerable force) from an area of high pressure to an area of low pressure",
      "partOfSpeech": "noun",
      "synonyms": [
        "air current",
        "current of air"
      ],
      "typeOf": [
        "weather",
        "weather condition",
        "atmospheric condition",
        "conditions"
      ],
      "hasTypes": [
        "blast",
        "blow",
        "boreas",
        "zephyr",
        "breeze",
        "calm",
        "calm air",
        "catabatic wind",
        "chinook",
        "chinook wind",
        "simoon",
        "sou'easter",
        "sou'wester",
        "air",
        "khamsin",
        "languor",
        "monsoon",
        "north wind",
        "norther",
        "northerly",
        "northwest wind",
        "northwester",
        "squall",
        "prevailing wind",
        "southwester",
        "southerly",
        "souther",
        "southeaster",
        "south wind",
        "samiel",
        "santa ana",
        "simoom",
        "snow eater",
        "crosswind",
        "doldrums",
        "draft",
        "draught",
        "east wind",
        "easter",
        "easterly",
        "airstream",
        "wester",
        "west wind",
        "foehn",
        "fohn",
        "gale",
        "gentle wind",
        "gust",
        "harmattan",
        "headwind",
        "high wind",
        "thermal",
        "tailwind",
        "katabatic wind"
      ],
      "hasSubstances": [
        "air"
      ],
      "derivation": [
        "windy"
      ],
      "examples": [
        "trees bent under the fierce winds",
        "when there is no wind, row"
      ]
    },
    {
      "definition": "coil the spring of (some mechanical device) by turning a stem",
      "partOfSpeech": "verb",
      "synonyms": [
        "wind up"
      ],
      "entails": [
        "turn"
      ],
      "typeOf": [
        "fasten",
        "tighten"
      ],
      "hasTypes": [
        "rewind"
      ],
      "derivation": [
        "winder"
      ],
      "examples": [
        "wind your watch"
      ]
    },
    {
      "definition": "an indication of potential opportunity",
      "partOfSpeech": "noun",
      "synonyms": [
        "confidential information",
        "hint",
        "lead",
        "steer",
        "tip"
      ],
      "typeOf": [
        "direction",
        "counsel",
        "counseling",
        "guidance",
        "counselling"
      ],
      "hasTypes": [
        "hasTypes4",
        "hasTypes3"
      ]
    },
    {
      "definition": "a tendency or force that influences events",
      "partOfSpeech": "noun",
      "typeOf": [
        "influence"
      ],
      "examples": [
        "the winds of change"
      ],
      "synonyms": [
        "synonyms3",
        "synonyms4"
      ],
      "hasTypes": [
        "hasTypes4",
        "hasTypes3"
      ]
    },
    {
      "definition": "breath",
      "partOfSpeech": "noun",
      "typeOf": [
        "expiration",
        "breathing out",
        "exhalation"
      ],
      "examples": [
        "the collision knocked the wind out of him"
      ],
      "synonyms": [
        "synonyms3",
        "synonyms4"
      ],
      "hasTypes": [
        "hasTypes4",
        "hasTypes3"
      ]
    }
  ],
  "syllables": {
    "count": 1,
    "list": [
      "wind"
    ]
  },
  "pronunciation": {
    "all": "wɪnd",
    "noun": "wɪnd",
    "verb": "waɪnd"
  },
  "frequency": 4.81
}
```

