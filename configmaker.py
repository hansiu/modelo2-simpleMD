#! /usr/bin/env/python
import configparser
import ast

def MakeConfig(NumAtoms=5,TimeStep=1,NumTimeSteps=10000,Algorithm='',PotList='',PotParameters='',Dimension=3):
    config=configparser.ConfigParser()
    config['DEFAULT'] = {}
    config['DEFAULT']['NumAtoms'] = str(NumAtoms)
    config['DEFAULT']['TimeStep'] = str(TimeStep)
    config['DEFAULT']['NumTimeSteps'] = str(NumTimeSteps)
    config['DEFAULT']['Algorithm'] = Algorithm
    config['DEFAULT']['Dimension'] = Dimension
    config['POTENTIALS'] = {}
    config['POTENTIALS']['PotList'] = str(PotList)
    config['POTENTIALS']['PotParameters'] = str(PotParameters)
    with open('config.ini','w') as configfile:
        config.write(configfile)
    
def ReadConfig():
    config=configparser.ConfigParser()
    config.read('config.ini')
    NumAtoms = ast.literal_eval(config['DEFAULT']['NumAtoms'])
    TimeStep = ast.literal_eval(config['DEFAULT']['TimeStep'])
    NumTimeSteps = ast.literal_eval(config['DEFAULT']['NumTimeSteps'])
    Algorithm = config['DEFAULT']['Algorithm']
    PotList = ast.literal_eval(config['POTENTIALS']['PotList'])
    PotParameters = ast.literal_eval(config['POTENTIALS']['PotParameters'])
    Dimension = ast.literal_eval(config['DEFAULT']['Dimension'])
    return((NumAtoms,TimeStep,NumTimeSteps,Algorithm,PotList,PotParameters,Dimension))