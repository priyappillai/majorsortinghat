import json
import math

with open("outdata.json", "r") as read_file:
    data = json.load(read_file)


def compareValues(userInput):
    print("userInput: "+str(userInput))
    resultScores = {}
    for major in data:
        tempScore = 0;
        print(major)
        for trait in userInput:
            if trait in data[str(major)]:
                print(trait)
                print(userInput[trait])
                print(str(major))
                print(data[str(major)])
                print(data[str(major)][trait]['Mean'])

                tempScore += (float(userInput[trait])-data[str(major)][trait]['Mean'])**2/(data[str(major)][trait]['SD']+0.001)
        resultScores[major] = math.sqrt(tempScore);
    #print(resultScores)
    print()
    invDict = invertDict(resultScores)
    #print(invDict)
    #print(dictToSortedList(invDict))

    for i in dictToSortedList(invDict):
        print(str(invDict[i]) +": "+ str(i))


def invertDict(d):
    newDict = {}
    for i in d.keys():
        newDict[d[i]] = i;
    return newDict

def dictToSortedList(d):
    mylist = list(d.keys())
    return (sorted(mylist))



def getInput():
    unprocessedInput = {}

    unprocessedInput["Like_Parties"] = input("Rate on a scale from 1-5 how much you like parties: ")
    
    unprocessedInput["Like_HangingOut"] = input("Rate on a scale from 1-5 how much you like Hanging out with friends: ")
    unprocessedInput["Like_Hiking"] = input("Rate on a scale from 1-5 how much you like Hiking: ")
    unprocessedInput["Like_BoardGames"] = input("Rate on a scale from 1-5 how much you like Board Games: ")
    unprocessedInput["Like_VideoGames"] = input("Rate on a scale from 1-5 how much you like Video Games: ")
    unprocessedInput["Like_WatchingTV"] = input("Rate on a scale from 1-5 how much you like watching TV: ")
    unprocessedInput["Like_WatchingMovies"] = input("Rate on a scale from 1-5 how much you like watching movies: ")
    unprocessedInput["Like_IndividualSports"] = input("Rate on a scale from 1-5 how much you like individual sports: ")
    unprocessedInput["Like_TeamSports"] = input("Rate on a scale from 1-5 how much you like team sports: ")
    unprocessedInput["Like_ReadingBook"] = input("Rate on a scale from 1-5 how much you like Reading a book: ")
    """
    unprocessedInput["PowerOfVulnerability"] = input("Rank on a scale from 1-5 how much you would like to watch the talk PowerOfVulnerability: ")
    unprocessedInput["FakeVideosOfRealPeople"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk FakeVideosOfRealPeople: ")
    unprocessedInput["PharmacyOfTheFuture"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk PharmacyOfTheFuture: ")
    unprocessedInput["HowGreatLeadersInspireGreatAction"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk HowGreatLeadersInspireGreatAction: ")
    unprocessedInput["LetMyDatasetChangeYourMindset"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk LetMyDatasetChangeYourMindset: ")
    unprocessedInput["MagicIngredientBringsLifeToPixar"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk MagicIngredientBringsLifeToPixar: ")
    unprocessedInput["PowerOfIntroverts"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk PowerOfIntroverts: ")
    unprocessedInput["WhatGardeningToldMeAboutLife"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk WhatGardeningToldMeAboutLife: ")
    unprocessedInput["WhatIfGentrificationWasAboutHealing"] = input(
        "Rank on a scale from 1-5 how much you would like to watch the talk WhatIfGentrificationWasAboutHealing: ")
    """
    return unprocessedInput



def fake6_2Input():
    data = {
    "Like_Parties": 1,
    "Like_HangingOut": 5,
    "Like_Hiking": 1,
    "Like_BoardGames": 2,
    "Like_VideoGames": 1,
    "Like_WatchingTV": 5,
    "Like_WatchingMovies": 5,
    "Like_IndividualSports": 1,
    "Like_TeamSports": 1,
    "Like_ReadingBook": 4,
    "PowerOfVulnerability": 4,
    "FakeVideosOfRealPeople": 1,
    "PharmacyOfTheFuture": 2,
    "HowGreatLeadersInspireGreatAction": 1,
    "LetMyDatasetChangeYourMindset": 2,
    "MagicIngredientBringsLifeToPixar": 5,
    "PowerOfIntroverts": 5,
    "WhatGardeningToldMeAboutLife": 1,
    "WhatIfGentrificationWasAboutHealing": 1,
    "HighSchool_Math": 4,
    "HighSchool_Physics": 3,
    "HighSchool_Chemistry": 4,
    "HighSchool_Bio": 1,
    "HighSchool_English": 2,
    "HighSchool_History": 1,
    "HighSchool_Music": 5,
    "HighSchool_Art": 5,
    "HighSchool_Leader": 3,
    "HighSchool_Engineering": 3,
    "Now_Math": 1,
    "Now_Physics": 1,
    "Now_Chemistry": 4,
    "Now_Bio": 2,
    "Now_English": 4,
    "Now_History": 1,
    "Now_Music": 5,
    "Now_Art": 5,
    "Now_Leader": 3,
    "Now_Engineering": 3,
    "Rank_Understand": 4,
    "Rank_FullOfIdeas": 5,
    "Rank_Imagination": 5,
    "Rank_DifficultyUnderstandingAbstract": 1,
    "Rank_AlwaysPrepared": 4,
    "Rank_AttentionToDetails": 4,
    "Rank_GetChoresDoneRightAway": 1,
    "Rank_ForgetToPutThingsBack": 4,
    "Rank_StartConversations": 1,
    "Rank_TalkToDifferentPeopleAtParties": 1,
    "Rank_ThinkALotBeforeSpeaking": 4,
    "Rank_DislikeGettingAttention": 5,
    "Rank_QuietAroundStrangers": 5,
    "Rank_SoftHeart": 5,
    "Rank_TakeTimeOutForOthers": 2,
    "Rank_MakePeopleFeelAtEase": 4,
    "Rank_NotInterestedInOthersProblems": 2,
    "Rank_FeelLittleConcernForOthers": 2,
    "Rank_GetIrritatedEasily": 2,
    "Rank_HaveFrequentMoodSwings": 2,
    "Rank_WorryAboutThings": 5,
    "Rank_RelaxedMostOfTheTime": 2,
    "Rank_SeldomFeelBlue": 2
  }
    return data


def fake12Input():
    data = {
        "Like_Parties": 4,
        "Like_HangingOut": 5,
        "Like_Hiking": 5,
        "Like_BoardGames": 3,
        "Like_VideoGames": 1,
        "Like_WatchingTV": 2,
        "Like_WatchingMovies": 3,
        "Like_IndividualSports": 2,
        "Like_TeamSports": 3,
        "Like_ReadingBook": 4,
        "PowerOfVulnerability": 2,
        "FakeVideosOfRealPeople": 3,
        "PharmacyOfTheFuture": 3,
        "HowGreatLeadersInspireGreatAction": 2,
        "LetMyDatasetChangeYourMindset": 3,
        "MagicIngredientBringsLifeToPixar": 3,
        "PowerOfIntroverts": 3,
        "WhatGardeningToldMeAboutLife": 4,
        "WhatIfGentrificationWasAboutHealing": 4,
        "HighSchool_Math": 4,
        "HighSchool_Physics": 4,
        "HighSchool_Chemistry": 5,
        "HighSchool_Bio": 5,
        "HighSchool_English": 3,
        "HighSchool_History": 2,
        "HighSchool_Music": 5,
        "HighSchool_Art": 4,
        "Now_Math": 4,
        "Now_Physics": 4,
        "Now_Chemistry": 4,
        "Now_Bio": 4,
        "Now_English": 4,
        "Now_History": 3,
        "Now_Music": 5,
        "Now_Art": 4,
        "Rank_Understand": 4,
        "Rank_FullOfIdeas": 3,
        "Rank_Imagination": 4,
        "Rank_DifficultyUnderstandingAbstract": 3,
        "Rank_AlwaysPrepared": 2,
        "Rank_AttentionToDetails": 5,
        "Rank_GetChoresDoneRightAway": 3,
        "Rank_ForgetToPutThingsBack": 3,
        "Rank_StartConversations": 2,
        "Rank_TalkToDifferentPeopleAtParties": 3,
        "Rank_ThinkALotBeforeSpeaking": 5,
        "Rank_DislikeGettingAttention": 4,
        "Rank_QuietAroundStrangers": 5,
        "Rank_SoftHeart": 4,
        "Rank_TakeTimeOutForOthers": 4,
        "Rank_MakePeopleFeelAtEase": 4,
        "Rank_NotInterestedInOthersProblems": 1,
        "Rank_FeelLittleConcernForOthers": 1,
        "Rank_GetIrritatedEasily": 1,
        "Rank_HaveFrequentMoodSwings": 2,
        "Rank_WorryAboutThings": 5,
        "Rank_RelaxedMostOfTheTime": 3,
        "Rank_SeldomFeelBlue": 3
    }
    return data


def fake2AInput():
    data = {
        "Like_Parties": 5,
        "Like_HangingOut": 5,
        "Like_Hiking": 3,
        "Like_BoardGames": 2,
        "Like_VideoGames": 3,
        "Like_WatchingTV": 2,
        "Like_WatchingMovies": 4,
        "Like_IndividualSports": 4,
        "Like_TeamSports": 5,
        "Like_ReadingBook": 3,
        "PowerOfVulnerability": 2,
        "FakeVideosOfRealPeople": 2,
        "PharmacyOfTheFuture": 3,
        "HowGreatLeadersInspireGreatAction": 5,
        "LetMyDatasetChangeYourMindset": 3,
        "MagicIngredientBringsLifeToPixar": 5,
        "PowerOfIntroverts": 3,
        "WhatGardeningToldMeAboutLife": 1,
        "WhatIfGentrificationWasAboutHealing": 1,
        "HighSchool_Math": 4,
        "HighSchool_Physics": 4,
        "HighSchool_Chemistry": 2,
        "HighSchool_Bio": 3,
        "HighSchool_English": 3,
        "HighSchool_History": 3,
        "HighSchool_Music": 5,
        "HighSchool_Art": 5,
        "Now_Math": 4,
        "Now_Physics": 4,
        "Now_Chemistry": 1,
        "Now_Bio": 3,
        "Now_English": 3,
        "Now_History": 3,
        "Now_Music": 5,
        "Now_Art": 5,
        "Now_Engineering": 4,
        "Rank_Understand": 3,
        "Rank_FullOfIdeas": 4,
        "Rank_Imagination": 4,
        "Rank_DifficultyUnderstandingAbstract": 3,
        "Rank_AlwaysPrepared": 4,
        "Rank_AttentionToDetails": 4,
        "Rank_GetChoresDoneRightAway": 2,
        "Rank_ForgetToPutThingsBack": 4,
        "Rank_StartConversations": 4,
        "Rank_TalkToDifferentPeopleAtParties": 4,
        "Rank_ThinkALotBeforeSpeaking": 4,
        "Rank_DislikeGettingAttention": 3,
        "Rank_QuietAroundStrangers": 4,
        "Rank_SoftHeart": 3,
        "Rank_TakeTimeOutForOthers": 4,
        "Rank_MakePeopleFeelAtEase": 5,
        "Rank_NotInterestedInOthersProblems": 2,
        "Rank_FeelLittleConcernForOthers": 2,
        "Rank_GetIrritatedEasily": 4,
        "Rank_HaveFrequentMoodSwings": 5,
        "Rank_WorryAboutThings": 5,
        "Rank_RelaxedMostOfTheTime": 1,
        "Rank_SeldomFeelBlue": 1
    }
    return data

def processInput(unprocessedInput):
    processedOutput = {}
    for i in unprocessedInput.keys():
        processedOutput[i] = float(unprocessedInput[i])-3
    return processedOutput

compareValues(processInput(fake6_2Input()))


userInput = {}

