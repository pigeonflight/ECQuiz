# -*- coding: cp1252 -*-
# This package is used to covert csv files to qti packages (zip files that contains qti xml files)
# The qti package that will be generated will have the following files:

# imsmanifest.xml --> This file defines the structure of the quiz and where each resources will be stored
# content/ -> This folder contains the questions as xml files which includes the answer and the format of each question

# This package is used in the Products ECQuiz package, processQTIImport function, when the Import event occurs in the import_export view for a quiz

import StringIO
import csv
from xml.etree.ElementTree import fromstring, ElementTree
import zipfile
import uuid

class CSVConverter: 
        def __init__(self, data):
                self.importXmls = []
                self.data = data
                self.qid = (uuid.uuid1()).hex
                self.items = ""
                self.resources = ""
                self.manifest = ""
                self.base = ""
                
        def processCSV(self):
                io = StringIO.StringIO(self.data)
                reader = csv.reader(io, delimiter=',', dialect="excel", quotechar='"')
                header = reader.next()
                mapping = ["question", "correct choice", "choice 1", "choice 2", "choice 3", "choice 4", "choice 5", "shuffle", "description"]
                def get_cell(row, number):
                        #read one cell on a @param row: CSV row as list
                        #param name: Column name: 1st row cell content value, header
                        title = number
                        question = row[0]
                        answers = ''
                        itemIndex = str(number)
                        resourceIndex = str((number-1))
                        uid = (uuid.uuid1()).hex
                        self.items += '<item identifier="TEST-1-ITEM-'+itemIndex+'" identifierref="UID-'+uid+'"><llsmc:weight>1</llsmc:weight><imsss:sequencing><imsss:randomizationControls randomizationTiming="onEachNewAttempt" reorderChildren="true"/></imsss:sequencing><llsmc:tutorGraded>false</llsmc:tutorGraded></item>'
                        self.resources += '<resource href="content/container0_question'+resourceIndex+'.xml" identifier="UID-'+uid+'" type="imsqti_item_xmlv2p0"><metadata><imsmd:lom><imsmd:general><imsmd:title><imsmd:langstring xml:lang="en">'+itemIndex+'</imsmd:langstring></imsmd:title></imsmd:general></imsmd:lom><imsqti:qtiMetadata><imsqti:interactionType>choiceInteraction</imsqti:interactionType></imsqti:qtiMetadata></metadata><file href="content/container0_question'+resourceIndex+'.xml"/></resource>'
                        for choice in range(2, 7):
                                if row[choice] != None:
                                        answers += '<simpleChoice identifier="Choice'+str((choice - 2))+'"><p>'+row[choice]+'</p></simpleChoice>'
                        
                        xml = '<?xml version="1.0" ?><assessmentItem false="adaptive" identifier="UID-'+uid+'" timeDependent="false" title="'+itemIndex+'" xmlns="http://www.imsglobal.org/xsd/imsqti_v2p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p0 http://www.imsglobal.org/xsd/imsqti_v2p0.xsd">'     
                        xml += '<outcomeDeclaration cardinality="single" identifier="OUTCOME"/>'
                        try:
                                xml += '<responseDeclaration cardinality="single" identifier="RESPONSE"><correctResponse><value>Choice'+str(int(row[1]) - 1)+'</value></correctResponse></responseDeclaration>'
                        except:
                                print "failed to append correct answer"
                        xml += '<itemBody><p>'+question+'</p>'
                        xml += '<choiceInteraction maxChoices="1" responseIdentifier="RESPONSE" shuffle="'+row[7]+'">'+answers+'</choiceInteraction></itemBody></assessmentItem>'
                        return xml                              
                row_id = 1
                for row in reader:
                        #try:
                        self.importXmls.append(get_cell(row, row_id))
                        #except:
                        #       print "Something went wrong during parsing in question stack "+str(row_id)
                        row_id += 1

#        def getQuestions(self):
#               for xml in self.importXmls:
#                       file = open("question.xml", "w")
#                       file.write(xml)
#                       file.close()
#                       ECQuiz.processQTIImport(file)
#               return "ok"

        def generateBase(self):
                self.base = '<?xml version="1.0" ?><assessmentItem adaptive="false" identifier="'+self.qid+'" timeDependent="false" title="default" xmlns="http://www.imsglobal.org/xsd/imsqti_v2p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p0 http://www.imsglobal.org/xsd/imsqti_v2p0.xsd"><itemBody/></assessmentItem>'

        def generateManifest(self):
                metadata = '<metadata><schema>IMS QTI</schema><schemaversion>2.0</schemaversion><imsqti:qtiMetadata><imsqti:toolName>LlsMultipleChoice</imsqti:toolName><imsqti:toolVersion>1.0</imsqti:toolVersion><imsqti:toolVendor>Alteroo Consulting Group</imsqti:toolVendor></imsqti:qtiMetadata><imsmd:lom><imsmd:general><imsmd:title><imsmd:langstring xml:lang="en">default</imsmd:langstring></imsmd:title></imsmd:general></imsmd:lom></metadata>'
                organisation = '<organizations><organization identifier="ORGANIZATION-1"><title>Default Organization</title><item identifier="TEST-1" identifierref="UID-'+self.qid+'">'+self.items+'<imsss:sequencing><imsss:randomizationControls reorderChildren="false"/></imsss:sequencing></item><imsss:sequencing><imsss:limitConditions attemptLimit="1"/><llsmc:instantFeedback>false</llsmc:instantFeedback><llsmc:oneQuestionPerPage>true</llsmc:oneQuestionPerPage><llsmc:allowNavigation>true</llsmc:allowNavigation></imsss:sequencing><llsmc:scoringFunction>guessing</llsmc:scoringFunction></organization></organizations>'
		default_resource ='<resource href="content/container0.xml" identifier="UID-'+self.qid+'" type="imsqti_item_xmlv2p0"><metadata><imsmd:lom><imsmd:general><imsmd:title><imsmd:langstring xml:lang="en">default</imsmd:langstring></imsmd:title> </imsmd:general></imsmd:lom></metadata><file href="content/container0.xml"/></resource>'
                resources = '<resources>'+default_resource+self.resources+'</resources>'
                self.manifest = '<?xml version="1.0" ?> <manifest identifier="MANIFEST-'+self.qid+'" xmlns="http://www.imsglobal.org/xsd/imscp_v1p1" xmlns:imsmd="http://www.imsglobal.org/xsd/imsmd_v1p2" xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_v2p0" xmlns:imsss="http://www.imsglobal.org/xsd/imsss" xmlns:llsmc="http://wwwai.cs.uni-magdeburg.de/llsmc/v1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p1.xsd http://www.imsglobal.org/xsd/imsmd_v1p2 http://www.imsglobal.org/xsd/imsmd_v1p2p2.xsd http://www.imsglobal.org/xsd/imsqti_v2p0 http://www.imsglobal.org/xsd/imsqti_v2p0.xsd">' + metadata + organisation + resources + '</manifest>'

        def generateZippedQuestions(self):          
                #try:                
                self.processCSV()
                self.generateBase()
                self.generateManifest()
		print "generating questions.zip"
                zf = zipfile.ZipFile("questions.zip", "w")
                zf.writestr("imsmanifest.xml", self.manifest)
                zf.writestr("content/container0.xml", self.base)
                index = 0
                for x in self.importXmls:
                        zf.writestr("content/container0_question"+str(index)+".xml", str(x))
                        index += 1
		return zf
                #except:
                #       print "invalid file, may not be a csv file"

