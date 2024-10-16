# -*- coding: utf-8 -*-

"""
wordsapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from wordsapi.api_helper import APIHelper


class WordDetails(object):

    """Implementation of the 'WordDetails' model.

    This custom type stores word information.

    Attributes:
        definition (str): Explains the definition of the word.
        part_of_speech (str): Explains what part of speech the word is.
        synonyms (List[str]): The list of synonyms.
        type_of (List[str]): List of words that are more general than the
            searched word.
        has_types (List[str]): More specific examples of types of searched
            word.
        derivation (List[str]): The derivation if any.
        examples (List[str]): The usage examples of word if any.
        antonyms (List[str]): List of antonyms for the searched word.
        verb_group (List[str]): The verb group of the searched word.
        has_parts (List[str]): Words that are parts of the searched word.
        has_substances (List[str]): Words that are substances of the searched
            word.
        entails (List[str]): Words that are implied by the searched word.
            Usually used for verbs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "definition": 'definition',
        "part_of_speech": 'partOfSpeech',
        "synonyms": 'synonyms',
        "type_of": 'typeOf',
        "has_types": 'hasTypes',
        "derivation": 'derivation',
        "examples": 'examples',
        "antonyms": 'antonyms',
        "verb_group": 'verbGroup',
        "has_parts": 'hasParts',
        "has_substances": 'hasSubstances',
        "entails": 'entails'
    }

    _optionals = [
        'definition',
        'part_of_speech',
        'synonyms',
        'type_of',
        'has_types',
        'derivation',
        'examples',
        'antonyms',
        'verb_group',
        'has_parts',
        'has_substances',
        'entails',
    ]

    def __init__(self,
                 definition=APIHelper.SKIP,
                 part_of_speech=APIHelper.SKIP,
                 synonyms=APIHelper.SKIP,
                 type_of=APIHelper.SKIP,
                 has_types=APIHelper.SKIP,
                 derivation=APIHelper.SKIP,
                 examples=APIHelper.SKIP,
                 antonyms=APIHelper.SKIP,
                 verb_group=APIHelper.SKIP,
                 has_parts=APIHelper.SKIP,
                 has_substances=APIHelper.SKIP,
                 entails=APIHelper.SKIP):
        """Constructor for the WordDetails class"""

        # Initialize members of the class
        if definition is not APIHelper.SKIP:
            self.definition = definition 
        if part_of_speech is not APIHelper.SKIP:
            self.part_of_speech = part_of_speech 
        if synonyms is not APIHelper.SKIP:
            self.synonyms = synonyms 
        if type_of is not APIHelper.SKIP:
            self.type_of = type_of 
        if has_types is not APIHelper.SKIP:
            self.has_types = has_types 
        if derivation is not APIHelper.SKIP:
            self.derivation = derivation 
        if examples is not APIHelper.SKIP:
            self.examples = examples 
        if antonyms is not APIHelper.SKIP:
            self.antonyms = antonyms 
        if verb_group is not APIHelper.SKIP:
            self.verb_group = verb_group 
        if has_parts is not APIHelper.SKIP:
            self.has_parts = has_parts 
        if has_substances is not APIHelper.SKIP:
            self.has_substances = has_substances 
        if entails is not APIHelper.SKIP:
            self.entails = entails 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        definition = dictionary.get("definition") if dictionary.get("definition") else APIHelper.SKIP
        part_of_speech = dictionary.get("partOfSpeech") if dictionary.get("partOfSpeech") else APIHelper.SKIP
        synonyms = dictionary.get("synonyms") if dictionary.get("synonyms") else APIHelper.SKIP
        type_of = dictionary.get("typeOf") if dictionary.get("typeOf") else APIHelper.SKIP
        has_types = dictionary.get("hasTypes") if dictionary.get("hasTypes") else APIHelper.SKIP
        derivation = dictionary.get("derivation") if dictionary.get("derivation") else APIHelper.SKIP
        examples = dictionary.get("examples") if dictionary.get("examples") else APIHelper.SKIP
        antonyms = dictionary.get("antonyms") if dictionary.get("antonyms") else APIHelper.SKIP
        verb_group = dictionary.get("verbGroup") if dictionary.get("verbGroup") else APIHelper.SKIP
        has_parts = dictionary.get("hasParts") if dictionary.get("hasParts") else APIHelper.SKIP
        has_substances = dictionary.get("hasSubstances") if dictionary.get("hasSubstances") else APIHelper.SKIP
        entails = dictionary.get("entails") if dictionary.get("entails") else APIHelper.SKIP
        # Return an object of this model
        return cls(definition,
                   part_of_speech,
                   synonyms,
                   type_of,
                   has_types,
                   derivation,
                   examples,
                   antonyms,
                   verb_group,
                   has_parts,
                   has_substances,
                   entails)
