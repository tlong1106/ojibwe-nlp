import random
from termcolor import colored
import time

def blue_text(text):
    return f"\033[34;01m{text}\033[00m"

def green_text(text):
    return f"\033[92;01m{text}\033[00m"

def red_text(text):
    return f"\033[31;01m{text}\033[00m"

def underline_text(text):
    return f"\033[04m{text}\033[00m"

class ConjugateVerb():
    def __init__(self, **kwargs):
        self.verb = kwargs.get("verb","error: verb")
        self.tense = kwargs.get("tense","error: tense")
        self.negation = kwargs.get("negation","error: negation")
        self.pronoun = kwargs.get("pronoun")
        self.answer_verb = kwargs.get("answer_verb","error: answer verb")
        self.color_verb = kwargs.get("color_verb","error: color verb")
        self.explanation = kwargs.get("explanation","error: explanation")

class ConjugateVII(ConjugateVerb):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def consonant_shift(self):
        con_shift = {"b":"p", "d":"t","g":"k","j":"ch","z":"s","zh":"sh"}
        short_vowels = ["a","i","o"]
        unvoiced_consonants = list(con_shift.values())
        voiced_consonants = list(con_shift.keys())
        if self.tense in ("past","future desiderative") and self.pronoun == None:
            # > > > vii logic goes here; update from intermediate ojibwe class
            pass
        elif self.tense in ("past","future desiderative") and self.pronoun != None:
            if self.tense == "past":
                if self.answer_verb[:3] in ("bak","gak"):
                    self.explanation.append("{} is an exception that does not change the first letter after {}{} prefix".format(self.answer_verb,blue_text(self.tense+" tense (did, was)"),blue_text(" | gii-")))
                elif self.answer_verb[0] in voiced_consonants and self.answer_verb[1] in short_vowels and self.answer_verb[2] in unvoiced_consonants:
                    self.explanation.append("some verbs are exceptions and do not change the first letter after {}{} because:\n".format(blue_text(self.tense+" tense (did, was)"),blue_text(" | gii-")))
                    self.explanation.append("{} in {}{} is a voiced consonant: {}".format(underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:],voiced_consonants))
                    self.explanation.append("{} in {}{}{} is a short vowel consonant: {}".format(underline_text(self.answer_verb[1]),self.answer_verb[0],underline_text(self.answer_verb[1]),self.answer_verb[2:],short_vowels))
                    self.explanation.append("{} in {}{}{} is an unvoiced consonant: {}\n".format(underline_text(self.answer_verb[2]),self.answer_verb[:2],underline_text(self.answer_verb[2]),self.answer_verb[3:],unvoiced_consonants))
                elif self.verb[:2] in list(con_shift.keys()):
                    self.explanation.append("{} changes {} in {} to {}{}".format(blue_text(self.tense+" tense (did, was)"),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2])+self.answer_verb[2:],underline_text(con_shift[self.answer_verb[:2]]),self.answer_verb[2:]))
                    self.answer_verb = con_shift[self.verb[:2]]+self.answer_verb[2:]
                    self.color_verb = con_shift[self.verb[:2]]+self.answer_verb[2:]
                    return self.answer_verb
                elif self.answer_verb[0] in con_shift.keys(): # and self.answer_verb[2] not in ("k","p","s","t"): << this needs to be updated 
                    self.explanation.append("{} changes {} in {} to {}{}".format(blue_text(self.tense+" tense (did, was)"),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0])+self.answer_verb[1:],underline_text(con_shift[self.answer_verb[0]]),self.answer_verb[1:]))
                    self.answer_verb = con_shift[self.verb[0]]+self.answer_verb[1:]
                    self.color_verb = con_shift[self.verb[0]]+self.answer_verb[1:]
                    return self.answer_verb
            elif self.tense == "future desiderative":
                if self.answer_verb[:3] in ("bak","gak"):
                    self.explanation.append("{} is an exception that does not change the first letter after {}{} prefix".format(self.answer_verb,blue_text(self.tense+" tense (will, going to)"),blue_text(" | wii-")))
                elif self.answer_verb[0] in voiced_consonants and self.answer_verb[1] in short_vowels and self.answer_verb[2] in unvoiced_consonants:
                    self.explanation.append("some verbs are exceptions and do not change the first letter after {}{} because:\n".format(blue_text(self.tense+" tense (will, going to)"),blue_text(" | wii-")))
                    self.explanation.append("{} in {}{} is a voiced consonant: {}".format(underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:],voiced_consonants))
                    self.explanation.append("{} in {}{}{} is a short vowel consonant: {}".format(underline_text(self.answer_verb[1]),self.answer_verb[0],underline_text(self.answer_verb[1]),self.answer_verb[2:],short_vowels))
                    self.explanation.append("{} in {}{}{} is an unvoiced consonant: {}\n".format(underline_text(self.answer_verb[2]),self.answer_verb[:2],underline_text(self.answer_verb[2]),self.answer_verb[3:],unvoiced_consonants))
                elif self.verb[:2] in list(con_shift.keys()):
                    self.explanation.append("{} changes {} in {} to {}{}".format(blue_text(self.tense+" tense (will, going to)"),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2])+self.answer_verb[2:],underline_text(con_shift[self.answer_verb[:2]]),self.answer_verb[2:]))
                    self.answer_verb = con_shift[self.verb[:2]]+self.answer_verb[2:]
                    self.color_verb = con_shift[self.verb[:2]]+self.answer_verb[2:]
                    return self.answer_verb
                elif self.answer_verb[0] in con_shift.keys():
                    self.explanation.append("{} changes {} in {} to {}{}".format(blue_text(self.tense+" tense (will, going to)"),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0])+self.answer_verb[1:],underline_text(con_shift[self.answer_verb[0]]),self.answer_verb[1:]))
                    self.answer_verb = con_shift[self.verb[0]]+self.answer_verb[1:]
                    self.color_verb = con_shift[self.verb[0]]+self.answer_verb[1:]
                    return self.answer_verb
        else:
            pass

    def tense_prefix(self):
        if self.tense == "present":
            self.tense = ""
            self.color_verb = self.answer_verb
            pass
        elif self.tense == "past":
            self.tense = "gii-"
            self.explanation.append("{} adds {} prefix to {}".format(blue_text("past tense (did, was)"),blue_text(self.tense),self.answer_verb))
            self.answer_verb = self.tense+self.answer_verb
            self.color_verb = colored(self.tense,"blue",attrs=["bold"])+self.answer_verb[len(self.tense):]
            return self.answer_verb
        elif self.tense == "future desiderative":
            self.tense = "wii-"
            self.explanation.append("{} adds {} prefix to {}".format(blue_text("future desiderative tense (will, going to)"),blue_text(self.tense),self.answer_verb))
            self.answer_verb = self.tense+self.answer_verb
            self.color_verb = colored(self.tense,"blue",attrs=["bold"])+self.answer_verb[len(self.tense):]
            return self.answer_verb
        elif self.tense == "future conditional":
            self.tense = "daa-"
            self.explanation.append("{} adds {} prefix to {}".format(blue_text("future conditional tense (could, should)"),blue_text(self.tense),self.answer_verb))
            self.answer_verb = self.tense+self.answer_verb
            self.color_verb = colored(self.tense,"blue",attrs=["bold"])+self.answer_verb[len(self.tense):]
            return self.answer_verb
        elif self.tense == "future definitive":
            if self.pronoun in ("1s","2s","1p","21","2p"):
                self.tense = "ga-"
                self.explanation.append("{} adds {} prefix to {}".format(blue_text("future definitive tense (will)"),blue_text(self.tense),self.answer_verb))
                self.answer_verb = self.tense+self.answer_verb
                self.color_verb = colored(self.tense,"blue",attrs=["bold"])+self.answer_verb[len(self.tense):]
                return self.answer_verb
            elif self.pronoun in ("3s","3p"):
                self.tense = "da-"
                self.explanation.append("{} adds {} prefix to {}".format(blue_text("future desiderative tense (will)"),blue_text(self.tense),self.answer_verb))
                self.answer_verb = self.tense+self.answer_verb
                self.color_verb = colored(self.tense,"blue",attrs=["bold"])+self.answer_verb[len(self.tense):]
                return self.answer_verb
        else:
            print("error in code! check for edge case in tense_prefix")

    def negation_suffix(self):
            if self.negation == False:
                pass
            elif self.negation == True and self.pronoun == None:
                # > > > vii logic goes here; update from intermediate ojibwe class
                pass
            elif self.negation == True and self.pronoun != None:
                if self.answer_verb[-1] in ("a","i","o","e"):
                    if self.pronoun in ("1s","2s","3s"):
                        self.negation_suffix = "siin"
                        if self.pronoun == "1s":
                            if self.answer_verb[-2:] in ("aa","ii","oo"):
                                self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("first person singular (niin | I)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                                self.answer_verb = self.answer_verb+self.negation_suffix
                                self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                                return self.answer_verb
                            elif self.answer_verb[-1] in ("a","i","o","e"):
                                self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("first person singular (niin | I)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                                self.answer_verb = self.answer_verb+self.negation_suffix
                                self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                                return self.answer_verb
                        elif self.pronoun == "2s":
                            if self.answer_verb[-2:] in ("aa","ii","oo"):
                                self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("second person singular (giin | you)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                                self.answer_verb = self.answer_verb+self.negation_suffix
                                self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                                return self.answer_verb
                            elif self.answer_verb[-1] in ("a","i","o","e"):
                                self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("second person singular (giin | you)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                                self.answer_verb = self.answer_verb+self.negation_suffix
                                self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                                return self.answer_verb
                        elif self.pronoun == "3s":
                            if self.answer_verb[-2:] in ("aa","ii","oo"):
                                self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("third person singular (wiin | she/he)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                                self.answer_verb = self.answer_verb+self.negation_suffix
                                self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                                return self.answer_verb
                            elif self.answer_verb[-1] in ("a","i","o","e"):
                                self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("second person singular (wiin | she/he)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                                self.answer_verb = self.answer_verb+self.negation_suffix
                                self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                                return self.answer_verb
                    elif self.pronoun in ("1p","21"):
                        self.negation_suffix = "siimin"
                        if self.pronoun == "1p":
                            if self.answer_verb[-2:] in ("aa","ii","oo"):
                                self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("first person plural exclusive (niinawind | we)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                                self.answer_verb = self.answer_verb+self.negation_suffix
                                self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                                return self.answer_verb
                            elif self.answer_verb[-1] in ("a","i","o","e"):
                                self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("first person plural exclusive (niinawind | we)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                                self.answer_verb = self.answer_verb+self.negation_suffix
                                self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                                return self.answer_verb
                        elif self.pronoun == "21":
                            if self.answer_verb[-2:] in ("aa","ii","oo"):
                                self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("first person plural inclusive (giinawind | we)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                                self.answer_verb = self.answer_verb+self.negation_suffix
                                self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                                return self.answer_verb
                            elif self.answer_verb[-1] in ("a","i","o","e"):
                                self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("first person plural inclusive (giinawind | we)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                                self.answer_verb = self.answer_verb+self.negation_suffix
                                self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                                return self.answer_verb
                    elif self.pronoun in ("2p"):
                        self.negation_suffix = "siim"
                        if self.answer_verb[-2:] in ("aa","ii","oo"):
                            self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("second person plural (giinawaa | you)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                            self.answer_verb = self.answer_verb+self.negation_suffix
                            self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                            return self.answer_verb
                        elif self.answer_verb[-1] in ("a","i","o","e"):
                            self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("second person plural (giinawaa | you)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                            self.answer_verb = self.answer_verb+self.negation_suffix
                            self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                            return self.answer_verb
                    elif self.pronoun in ("3p"):
                        self.negation_suffix = "siiwag"
                        # < < <
                        if self.answer_verb[-2:] in ("aa","ii","oo"):
                            self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("third person plural (wiinawaa | they)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                            self.answer_verb = self.answer_verb+self.negation_suffix
                            self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                            return self.answer_verb
                        elif self.answer_verb[-1] in ("a","i","o","e"):
                            self.explanation.append("when {}, {} adds {} suffix after {} in {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("third person plural (wiinawaa | they)"),red_text(self.negation_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                            self.answer_verb = self.answer_verb+self.negation_suffix
                            self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                            return self.answer_verb
                    else:
                        return print("error in code! check negation_suffix for vowels")
                elif self.answer_verb[-2:] == "am":
                    if self.pronoun in ("1s","2s","3s"):
                        self.negation_suffix = "nziin"
                        if self.pronoun == "1s":
                            self.explanation.append("when {}, {} drops {} from {}{} and adds {} suffix".format(red_text("negated (didn't, don't, won't)"),green_text("first person singular (niin | I)"),underline_text(self.answer_verb[-1]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:]),red_text(self.negation_suffix)))
                        elif self.pronoun == "2s":
                            self.explanation.append("when {}, {} drops {} from {}{} and adds {} suffix".format(red_text("negated (didn't, don't, won't)"),green_text("second person singular (giin | you)"),underline_text(self.answer_verb[-1]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:]),red_text(self.negation_suffix)))
                        elif self.pronoun == "3s":
                            self.explanation.append("when {}, {} drops {} from {}{} and adds {} suffix".format(red_text("negated (didn't, don't, won't)"),green_text("third person singular (wiin | she/he)"),underline_text(self.answer_verb[-1]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:]),red_text(self.negation_suffix)))
                        self.answer_verb = self.answer_verb[:-1]+self.negation_suffix
                        self.color_verb = self.color_verb[:-1]+colored(self.negation_suffix,"red",attrs=["bold"])
                        return self.answer_verb
                    elif self.pronoun in ("1p","21"):
                        self.negation_suffix = "nziimin"
                        if self.pronoun == "1p":
                            self.explanation.append("when {}, {} drops {} from {}{} and adds {} suffix".format(red_text("negated (didn't, don't, won't)"),green_text("first person plural exclusive (niinawind | we)"),underline_text(self.answer_verb[-1]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:]),red_text(self.negation_suffix)))
                        elif self.pronoun == "21":
                            self.explanation.append("when {}, {} drops {} from {}{} and adds {} suffix".format(red_text("negated (didn't, don't, won't)"),green_text("first person plural inclusive (giinawind | we)"),underline_text(self.answer_verb[-1]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:]),red_text(self.negation_suffix)))
                        self.answer_verb = self.answer_verb[:-1]+self.negation_suffix
                        self.color_verb = self.color_verb[:-1]+colored(self.negation_suffix,"red",attrs=["bold"])
                        return self.answer_verb
                    elif self.pronoun in ("2p"):
                        self.negation_suffix = "nziim"
                        self.explanation.append("when {}, {} drops {} from {}{} and adds {} suffix".format(red_text("negated (didn't, don't, won't)"),green_text("second person plural (giinawaa | you)"),underline_text(self.answer_verb[-1]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:]),red_text(self.negation_suffix)))
                        self.answer_verb = self.answer_verb[:-1]+self.negation_suffix
                        self.color_verb = self.color_verb[:-1]+colored(self.negation_suffix,"red",attrs=["bold"])
                        return self.answer_verb
                    elif self.pronoun in ("3p"):
                        self.negation_suffix = "nziiwag"
                        self.explanation.append("when {}, {} drops {} from {}{} and adds {} suffix".format(red_text("negated (didn't, don't, won't)"),green_text("third person plural (wiinawaa | they)"),underline_text(self.answer_verb[-1]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:]),red_text(self.negation_suffix)))
                        self.answer_verb = self.answer_verb[:-1]+self.negation_suffix
                        self.color_verb = self.color_verb[:-1]+colored(self.negation_suffix,"red",attrs=["bold"])
                        return self.answer_verb
                    else:
                        return print("error in code! check negation_suffix for 'am' ending")
                elif self.answer_verb[-2:] == "in":
                    if self.pronoun in ("1s","2s","3s"):
                        self.negation_suffix = "ziin"
                        if self.pronoun == "1s":
                            self.explanation.append("when {}, {} adds {} suffix after {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("first person singular (niin | I)"),red_text(self.negation_suffix),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        elif self.pronoun == "2s":
                            self.explanation.append("when {}, {} adds {} suffix after {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("second person singular (giin | you)"),red_text(self.negation_suffix),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        elif self.pronoun == "3s":
                            self.explanation.append("when {}, {} adds {} suffix after {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("third person singular (wiin | she/he)"),red_text(self.negation_suffix),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        self.answer_verb = self.answer_verb+self.negation_suffix
                        self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                        return self.answer_verb
                    elif self.pronoun in ("1p","21"):
                        self.negation_suffix = "ziimin"
                        if self.pronoun == "1p":
                            self.explanation.append("when {}, {} adds {} suffix after {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("first person plural exclusive (niinawind | we)"),red_text(self.negation_suffix),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        elif self.pronoun == "21":
                            self.explanation.append("when {}, {} adds {} suffix after {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("first person plural inclusive (giinawind | we)"),red_text(self.negation_suffix),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        self.answer_verb = self.answer_verb+self.negation_suffix
                        self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                        return self.answer_verb
                    elif self.pronoun in ("2p"):
                        self.negation_suffix = "ziim"
                        self.explanation.append("when {}, {} adds {} suffix after {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("second person plural (giinawaa | you)"),red_text(self.negation_suffix),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        self.answer_verb = self.answer_verb+self.negation_suffix
                        self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                        return self.answer_verb
                    elif self.pronoun in ("3p"):
                        self.negation_suffix = "ziiwag"
                        self.explanation.append("when {}, {} adds {} suffix after {}{}".format(red_text("negated (didn't, don't, won't)"),green_text("third person plural (wiinawaa | they)"),red_text(self.negation_suffix),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        self.answer_verb = self.answer_verb+self.negation_suffix
                        self.color_verb = self.color_verb+colored(self.negation_suffix,"red",attrs=["bold"])
                        return self.answer_verb
                    else:
                        return print("error in code! check negation_suffix for 'in' ending")
                else:
                    print("error in code! check for edge case in negation_suffix")

    def conjugate_vii(self):
        verb.consonant_shift()
        verb.tense_prefix()
        verb.negation_suffix()
        return self.answer_verb

class ConjugateVAI(ConjugateVII):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def drop_short_vowel(self):
        if self.pronoun in ("1s","2s") and self.verb[-1] in ("a","i","o") and self.verb[-2:] not in ("aa","ii","oo") and verb.negation == False:
            if self.pronoun == "1s":
                self.explanation.append("{} drops final short vowel {} from {}{}".format(green_text("first person singular (niin | I)"),underline_text(self.verb[-1]),self.verb[:-1],underline_text(self.verb[-1])))
                self.answer_verb = self.verb[:-1]
                return self.answer_verb
            elif self.pronoun == "2s":
                self.explanation.append("{} drops final short vowel {} from {}{}".format(green_text("second person singular (giin | you)"),underline_text(self.verb[-1]),self.verb[:-1],underline_text(self.verb[-1])))
                self.answer_verb = self.verb[:-1]
                return self.answer_verb
        else:
            self.answer_verb = self.verb
            return self.answer_verb

    def pronoun_prefix(self):
        if self.pronoun in ("3s","3p"):
            pass
        elif self.answer_verb[0] == "b":
            if self.pronoun in ("1s","1p"):
                self.pronoun_prefix = "nim"
                if self.pronoun == "1s":
                    self.explanation.append("{} adds {}{} prefix before {} in {}{}".format(green_text("first person singular (niin | I)"),green_text("in, ni, "),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "1p":
                    self.explanation.append("{} adds {}{} prefix before {} in {}{}".format(green_text("first person plural exclusive (niinawind | we)"),green_text("in, ni, "),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                self.answer_verb = self.pronoun_prefix+self.answer_verb
                self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                return self.answer_verb
            elif self.pronoun in ("2s","21","2p"):
                self.pronoun_prefix = "gi"
                if self.pronoun == "2s":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person singular (giin | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "21":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person plural inclusive (giinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "2p":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person plural (giinawaa | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                self.answer_verb = self.pronoun_prefix+self.answer_verb
                self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                return self.answer_verb
            else:
                print("error in code! check for edge case in 'b' pronoun_prefix")
        elif self.answer_verb[0] in ("m","n","w"):
            if self.pronoun in ("1s","1p"):
                self.pronoun_prefix = "ni"
                if self.pronoun == "1s":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person singular (niin | I)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "1p":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person plural exclusive (niinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                self.answer_verb = self.pronoun_prefix+self.answer_verb
                self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                return self.answer_verb
            elif self.pronoun in ("2s","21","2p"):
                self.pronoun_prefix = "gi"
                if self.pronoun == "2s":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person singular (giin | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "21":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person plural inclusive (giinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "2p":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person plural (giinawaa | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                self.answer_verb = self.pronoun_prefix+self.answer_verb
                self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                return self.answer_verb
            else:
                print("error in code! check for edge case in 'm', 'n', 'w' pronoun_prefix")
        elif self.answer_verb[:2] in ("ch","sh","zh") or self.answer_verb[0] in ("d","g","j","z"):
            if self.pronoun in ("1s","1p"):
                self.pronoun_prefix = "nin"
                if self.pronoun == "1s":
                    if self.answer_verb[:2] in ("ch","sh","zh"):
                        self.explanation.append("{} adds {}{} prefix before {} in {}{}".format(green_text("first person singular (niin | I)"),green_text("in, ni, "),green_text(self.pronoun_prefix),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2]),self.answer_verb[2:]))
                    else:
                        self.explanation.append("{} adds {}{} prefix before {} in {}{}".format(green_text("first person singular (niin | I)"),green_text("in, ni, "),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "1p":
                    if self.answer_verb[:2] in ("ch","sh","zh"):
                        self.explanation.append("{} adds {}{} prefix before {} in {}{}".format(green_text("first person plural exclusive (niinawind | we)"),green_text("in, ni, "),green_text(self.pronoun_prefix),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2]),self.answer_verb[2:]))
                    else:
                        self.explanation.append("{} adds {}{} prefix before {} in {}{}".format(green_text("first person plural exclusive (niinawind | we)"),green_text("in, ni, "),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                self.answer_verb = self.pronoun_prefix+self.answer_verb
                self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                return self.answer_verb
            elif self.pronoun in ("2s","21","2p"):
                self.pronoun_prefix = "gi"
                if self.pronoun == "2s":
                    if self.answer_verb[:2] in ("ch","sh","zh"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person singular (giin | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2]),self.answer_verb[2:]))
                    else:
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person singular (giin | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "21":
                    if self.answer_verb[:2] in ("ch","sh","zh"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person plural inclusive (giinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2]),self.answer_verb[2:]))
                    else:
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person plural inclusive (giinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "2p":
                    if self.answer_verb[:2] in ("ch","sh","zh"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person plural (giinawaa | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2]),self.answer_verb[2:]))
                    else:
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person plural (giinawaa | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                self.answer_verb = self.pronoun_prefix+self.answer_verb
                self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                return self.answer_verb
            else:
                print("error in code! check for edge case in 'd', 'g', 'j', 'z', 'zh' pronoun_prefix")
        elif self.answer_verb[:2] == "oo" or (self.answer_verb[0] != "o" and self.answer_verb[0] in ("a","i","e")):
            if self.pronoun in ("1s","1p"):
                self.pronoun_prefix = "nind"
                if self.pronoun == "1s":
                    if self.answer_verb[:2] in ("aa","ii","oo"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person singular (niin | I)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2]),self.answer_verb[2:]))
                        self.answer_verb = self.pronoun_prefix+self.answer_verb
                        self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                        return self.answer_verb
                    elif self.answer_verb[0] in ("a","i","o","e"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person singular (niin | I)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                        self.answer_verb = self.pronoun_prefix+self.answer_verb
                        self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                        return self.answer_verb
                elif self.pronoun == "1p":
                    if self.answer_verb[:2] in ("aa","ii","oo"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person plural (niinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2]),self.answer_verb[2:]))
                        self.answer_verb = self.pronoun_prefix+self.answer_verb
                        self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                        return self.answer_verb
                    elif self.answer_verb[0] in ("a","i","o","e"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person plural (niinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                        self.answer_verb = self.pronoun_prefix+self.answer_verb
                        self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                        return self.answer_verb
            elif self.pronoun in ("2s","21","2p"):
                self.pronoun_prefix = "gid"
                if self.pronoun == "2s":
                    if self.answer_verb[:2] in ("aa","ii","oo"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person singular (giin | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2]),self.answer_verb[2:]))
                        self.answer_verb = self.pronoun_prefix+self.answer_verb
                        self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                        return self.answer_verb
                    elif self.answer_verb[0] in ("a","i","o","e"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person singular (giin | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                        self.answer_verb = self.pronoun_prefix+self.answer_verb
                        self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                        return self.answer_verb
                elif self.pronoun == "21":
                    if self.answer_verb[:2] in ("aa","ii","oo"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person plural inclusive (giinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2]),self.answer_verb[2:]))
                        self.answer_verb = self.pronoun_prefix+self.answer_verb
                        self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                        return self.answer_verb
                    elif self.answer_verb[0] in ("a","i","o","e"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person plural inclusive (giinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                        self.answer_verb = self.pronoun_prefix+self.answer_verb
                        self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                        return self.answer_verb
                elif self.pronoun == "2p":
                    if self.answer_verb[:2] in ("aa","ii","oo"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person plural (giinawaa | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[:2]),underline_text(self.answer_verb[:2]),self.answer_verb[2:]))
                        self.answer_verb = self.pronoun_prefix+self.answer_verb
                        self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                        return self.answer_verb
                    elif self.answer_verb[0] in ("a","i","o","e"):
                        self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person plural (giinawaa | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                        self.answer_verb = self.pronoun_prefix+self.answer_verb
                        self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                        return self.answer_verb
            else:
                print("error in code! check for edge case in 'oo' and non-'o' vowels pronoun_prefix")
        elif self.answer_verb[0] == "o":
            if self.pronoun in ("1s","1p"):
                self.pronoun_prefix = "nindo"
                if self.pronoun == "1s":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person singular (niin | I)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "1p":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person plural exclusive (niinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                self.answer_verb = self.pronoun_prefix+self.answer_verb
                self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                return self.answer_verb
            elif self.pronoun in ("2s","21","2p"):
                self.pronoun_prefix = "gido"
                if self.pronoun == "2s":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person singular (giin | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "21":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("first person plural inclusive (giinawind | we)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                elif self.pronoun == "2p":
                    self.explanation.append("{} adds {} prefix before {} in {}{}".format(green_text("second person plural (giinawaa | you)"),green_text(self.pronoun_prefix),underline_text(self.answer_verb[0]),underline_text(self.answer_verb[0]),self.answer_verb[1:]))
                self.answer_verb = self.pronoun_prefix+self.answer_verb
                self.color_verb = colored(self.pronoun_prefix,"green",attrs=["bold"])+self.color_verb
                return self.answer_verb
            else:
                print("error in code! check for edge case in 'o' pronoun_prefix")
        else:
            print("error in code! check for edge case in pronoun_prefix")
    
    def pronoun_suffix(self):
        if self.negation == True:
            pass
        elif self.negation == False:
            if self.pronoun in ("1p","21"):
                if self.answer_verb[-1] in ("a","i","o","e") or self.verb[-1] == "g":
                    self.pronoun_suffix = "min"
                    if self.answer_verb[-2:] in ("aa","ii","oo"):
                        if self.pronoun == "1p":
                            self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("first person plural exclusive (niinawind | we)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                            self.answer_verb = self.answer_verb+self.pronoun_suffix
                            self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                            return self.answer_verb
                        elif self.pronoun == "21":
                            self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("first person plural inclusive (giinawind | we)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                            self.answer_verb = self.answer_verb+self.pronoun_suffix
                            self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                            return self.answer_verb
                    if self.answer_verb[-1] in ("a","i","o","e","g"):
                        if self.pronoun == "1p":
                            self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("first person plural exclusive (niinawind | we)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                            self.answer_verb = self.answer_verb+self.pronoun_suffix
                            self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                            return self.answer_verb
                        elif self.pronoun == "21":
                            self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("first person plural inclusive (giinawind | we)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                            self.answer_verb = self.answer_verb+self.pronoun_suffix
                            self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                            return self.answer_verb
                elif self.answer_verb[-2:] == "am":
                    self.pronoun_suffix = "aam"
                    if self.pronoun == "1p":
                        self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("first person plural exclusive (niinawind | we)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                    elif self.pronoun == "21":
                        self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("first person plural inclusive (niinawind | we)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                    self.answer_verb = self.answer_verb[:-2]+self.pronoun_suffix
                    self.color_verb = self.color_verb[:-2]+colored(self.pronoun_suffix,"green",attrs=["bold"])
                    return self.answer_verb
                elif self.answer_verb[-2:] == "in":
                    self.pronoun_suffix = "imin"
                    if self.pronoun == "1p":
                        self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("first person plural exclusive (niinawind | we)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                    elif self.pronoun == "21":
                        self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("first person plural inclusive (niinawind | we)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                    self.answer_verb = self.answer_verb+self.pronoun_suffix
                    self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                    return self.answer_verb
                else:
                    return print(red_text("edge case! check pronoun_suffix for 1p, 21"))
            elif self.pronoun in ("2p"):
                if self.answer_verb[-1] in ("a","i","o","e") or self.verb[-1] == "g":
                    self.pronoun_suffix = "m"
                    if self.answer_verb[-2:] in ("aa","ii","oo"):
                        self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("second person plural (giinawaa | you)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        self.answer_verb = self.answer_verb+self.pronoun_suffix
                        self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                        return self.answer_verb
                    elif self.answer_verb[-1] in ("a","i","o","e","g"):
                        self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("second person plural (giinawaa | you)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                        self.answer_verb = self.answer_verb+self.pronoun_suffix
                        self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                        return self.answer_verb
                elif self.answer_verb[-2:] == "am":
                    self.pronoun_suffix = "aam"
                    self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("second person plural (giinawaa | you)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                    self.answer_verb = self.answer_verb[:-2]+self.pronoun_suffix
                    self.color_verb = self.color_verb[:-2]+colored(self.pronoun_suffix,"green",attrs=["bold"])
                    return self.answer_verb
                elif self.answer_verb[-2:] == "in":
                    self.pronoun_suffix = "im"
                    self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("second person plural (giinawaa | you)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                    self.answer_verb = self.answer_verb+self.pronoun_suffix
                    self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                    return self.answer_verb
                else:
                    return print(red_text("error in code! check pronoun_suffix for 2p"))
            elif self.pronoun == "3p":
                if self.answer_verb[-1] in ("a","i","o","e") or self.verb[-1] == "g":
                    self.pronoun_suffix = "wag"
                    if self.answer_verb[-2:] in ("aa","ii","oo"):
                        self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("third person plural (wiinawaa | they)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        self.answer_verb = self.answer_verb+self.pronoun_suffix
                        self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                        return self.answer_verb
                    elif self.answer_verb[-1] in ("a","i","o","e","g"):
                        self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("third person plural (wiinawaa | they)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-1]),self.answer_verb[:-1],underline_text(self.answer_verb[-1])))
                        self.answer_verb = self.answer_verb+self.pronoun_suffix
                        self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                        return self.answer_verb
                elif self.answer_verb[-2:] in ("am","in"):
                    self.pronoun_suffix = "oog"
                    if self.answer_verb[-2:] == "am":
                        self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("third person plural (wiinawaa | they)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        self.answer_verb = self.answer_verb+self.pronoun_suffix
                        self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                        return self.answer_verb
                    elif self.answer_verb[-2:] == "in":
                        self.explanation.append("{} adds {} suffix after {} in {}{}".format(green_text("third person plural (wiinawaa | they)"),green_text(self.pronoun_suffix),underline_text(self.answer_verb[-2:]),self.answer_verb[:-2],underline_text(self.answer_verb[-2:])))
                        self.answer_verb = self.answer_verb+self.pronoun_suffix
                        self.color_verb = self.color_verb+colored(self.pronoun_suffix,"green",attrs=["bold"])
                        return self.answer_verb
                else:
                    return print(red_text("error in code! check pronoun_suffix for 3p"))
        else:
            print("error in code! check for edge case in pronoun_suffix")
  
    def conjugate_vai(self):
        verb.drop_short_vowel()
        verb.consonant_shift()
        verb.tense_prefix()
        verb.pronoun_prefix()
        verb.pronoun_suffix()
        verb.negation_suffix()
        return self.answer_verb

# - - - - - - - - - - - - - - - - - - - - - - - - ui code starts here - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# edge case: oodenawi'idiwag

# import pandas dataframe here

n = 1
while n > 0:

    # consider a menu to group nouns, verbs of specific vocabulary (weather, clothing; chores, household items; exploring outdoors, trees, animals; etc.)

    verbTypeList = ["vii","vai"] #
    randVerbType = random.choice(verbTypeList)

    tenseList = ["present","past","future desiderative","future definitive","future conditional"]
    pronounList = ["1s","2s","3s","1p","21","2p","3p"]
    negationList = [True,False]

    if randVerbType == "vii":
        # update verbList to include filtered pandas dataframe for vii
        verbList = ["gimiwan","zoogipon","mizhakwad"]
        randOptions = random.choice(verbList),random.choice(tenseList),random.choice(negationList)
        print(f"\nverb: {randOptions[0]}\ntense: {blue_text(randOptions[1])}\nnegation: {red_text(randOptions[2])}")
        verb = ConjugateVII(verb=randOptions[0],tense=randOptions[1],negation=randOptions[2],answer_verb="",color_verb="",explanation=[])
        verb.conjugate_vii()
    elif randVerbType == "vai":
        # update verbList to include filtered pandas dataframe for vai
        verbList = ["wiisini","bakade","giishkaabaagwe","debisinii","jiibaakwe"]
        randOptions = random.choice(verbList),random.choice(tenseList),random.choice(negationList),random.choice(pronounList)
        print(f"\nverb: {randOptions[0]}\ntense: {blue_text(randOptions[1])}\nnegation: {red_text(randOptions[2])}\npronoun: {green_text(randOptions[3])}")
        verb = ConjugateVAI(verb=randOptions[0],tense=randOptions[1],negation=randOptions[2],pronoun=randOptions[3],answer_verb="",color_verb="",explanation=[])
        verb.conjugate_vai()

    # user response
    # print("\n[user response here]\n")
    user_response = input("\ntype response here: ")
    if user_response == "quit":
        break
    elif user_response == verb.answer_verb:
        print("\ncorrect!\n")
    else:
        print("\nincorrect...\n")
        print("explanation:\n")
        for step in verb.explanation:
            time.sleep(1)
            print(step)
        time.sleep(1)

    def neg(word):
        if verb.negation == True:
            negated = colored("gaawiin","red",attrs=["bold"])
            negated = negated+" "+verb.color_verb
            return negated
        else:
            return verb.color_verb

    print("\nsolution:",neg(verb.color_verb),"\n")