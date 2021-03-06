# Author: Dr. Avner OTTENSOOSER
# Copyrights: Creative Commons
# Decription: This program loops throug a list of all the books in teh old testemony, finds thier lingustic diversity
#             and commonality of volcubelty. The program then plost the data on control charts.
from __future__ import division
import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
from rpy import *
import os
import shutil 
def main():

    # Book Taple = Nice Name, Short Name, Last Chapter, Last verse in the last chapter

    # TODO - put this in a database

    AO_tBooks=[ 
               ('Genesis',      'Gen',        50,26),
               ('Exodus',       'Ex',         40,38),
               ('Leviticus',    'Lev',        27,34),
               ('Numbers',      'Num',        36,13),
               ('Deuteronomy',  'Deut',       34,12),
               ('Joshua',       'Josh',       24,33),
               ('Judges',       'Judg',       21,25),
               ('Samuel 1',     '1 Sam',      31,13),
               ('Samuel 2',     '2 Sam',      24,24),
               ('Kings 1',      '1 Kings',    22,54),
               ('Kings 2',      '2 Kings',    22,54),
               ('Isaia',        'Isa',        66,24),
               ('Jeremiah',     'Jer',        52,34),
               ('Ezekiel',      'Ezek',       48,35),
               ('Hosea',        'Hos',        14,10),
               ('Joel',         'Joel',        4,21),
               ('Amos',         'Am',          9,15),
               ('Obadiah',      'Ob',          1,21),
               ('Jonah',        'Jon',         4,11),
               ('Micah',        'Mic',         7,20),
               ('Nahum',        'Nah',         3,19),
               ('Habakkuk',     'Hab',         3,19),
               ('Zephaniah',    'Zeph',        3,20),
               ('Haggai',       'Hag',         2,23),
               ('Zechariah',    'Zech',       14,21),
               ('Malachi',      'Mal',         3,24),
               ('Psalms',       'Ps',         150,6),
               ('Proverbs',     'Prov',       31,22),
               ('Job',          'Job',        42,17),
               ('Song of Songs','Song',        8,14),
               ('Ruth',         'Ruth',        4,22),
               ('Lamentations', 'Lam',         5,22),
               ('Ecclesiastes', 'Eccl',       12,14),
               ('Esther',       'Esth',       10,3),
               ('Daniel',       'Dan',        12,13),
               ('Ezra',         'Ezra',       10,44),
               ('Nehemiah',     'Neh',        13,31),
               ('Chronicles 1', '1 Chr',      29,30),
               ('Chronicles 2', '2 Chr',      36,23)
              ]              

    # home folder
    AO_sCompelationSite = 'C:\\Users\\Avner\\SkyDrive\\NLP\\BiblicalNLPworks\\'

    # Calculate the name of the files
    AO_ModulesPass   =  AO_sCompelationSite + 'Source Code'
    AO_sGraphsPass = AO_sCompelationSite +'Graphs\\Volcublary comparison\\'

    AO_s10ersGraphsPass = AO_sCompelationSite +'Graphs\\10ers\\'
    if not os.path.exists(AO_s10ersGraphsPass):
        os.makedirs(AO_s10ersGraphsPass)


    # Manage the file that will include statistical freeks (the data is appended to this file in AO_mNLTK.AO_bMTLookForLowPobabilirty
    A0_sCSVpath = AO_sCompelationSite +'Data\\CSV\\'
    # ensure that the CSV folder exists
    if not os.path.exists(A0_sCSVpath):
        os.makedirs(A0_sCSVpath)

    AO_s10ersFileName = A0_sCSVpath +'10ers.CSV' 

    if  os.path.exists(AO_s10ersFileName):
        os.remove(AO_s10ersFileName)
    

    AO_s10erGraphsFolde  = AO_sCompelationSite +'Graphs\\10ers\\'

    # alter the DOS path
    # sys.path.append(AO_ModulesPass)
    # load my modules
    import AO_mNLTK, AO_mPopularWords, AO_mBookLoader


    


    AO_lBookAvarageWordLegpgthByChapter = []
    AO_lJchapter = []
    AO_l10er = []
    AO_l10erStart = [-1,-1]
    
    # for all the books in the J Bible    
    for AO_iJBook in range (0,len(AO_tBooks)):
        if AO_tBooks[AO_iJBook][2] > 10: #no need to look at short books
            AO_sJBook = AO_tBooks[AO_iJBook][0]
            A0_iLastJBookChapter = AO_tBooks[AO_iJBook][2]
            print(AO_sJBook)
            AO_lLigusticDiversity = AO_mNLTK.AO_fNLP(AO_sJBook,AO_tBooks[AO_iJBook][1],A0_iLastJBookChapter,AO_tBooks[AO_iJBook][3])
            AO_lCommonWordUsage = AO_mPopularWords.AO_fPopularWords(AO_sJBook,AO_tBooks[AO_iJBook][1],A0_iLastJBookChapter,AO_tBooks[AO_iJBook][3])
            # for l in range (0, len( AO_lLigusticDiversity)):
            #    print str(AO_lLigusticDiversity[l]) + " "
            #print "\n"

            #########################################
            # Graph 1
            #########################################

            if AO_lLigusticDiversity > 1:
                AO_fSd = r.sd(AO_lLigusticDiversity)
            else:
                AO_lLigusticDiversity = 0
                
            AO_fMean = r.mean(AO_lLigusticDiversity)



            # plot a triangle for each chapter's linguistic diversity
            # No 0 chapter 
            x = np.arange(1, len(AO_lLigusticDiversity)+1, 1);
            y = AO_lLigusticDiversity

            # Analyse the vecror for 10ers
            AO_l10erStart = AO_mNLTK.AO_lMTLookForLowPobabilirty(y,AO_sJBook,'Linguistic Divercity',AO_fMean,AO_s10ersFileName)

            if AO_l10erStart[0] > 0:
                
                fig10erA, = plt.plot([AO_l10erStart[0],AO_l10erStart[0]], [r.min(AO_lLigusticDiversity),r.max(AO_lLigusticDiversity)])
                fig10erB, = plt.plot([AO_l10erStart[1],AO_l10erStart[1]], [r.min(AO_lLigusticDiversity),r.max(AO_lLigusticDiversity)])

            # plot!
            fig1, = plt.plot(x, y, 'g^')
            
            

        
           
            # plot a line at the mean
            for m in range (0, len(x)):
                y[m]=AO_fMean
            fig2, = plt.plot(x, y)



            # plot upper control  line at two standard deviations
            for m in range (0, len(x)):
                y[m]=2*AO_fSd + AO_fMean
            fig3, =plt.plot(x, y)

            #  plot lower control  line at two standard deviations
            for m in range (0, len(x)):
                y[m] = AO_fMean - 2*AO_fSd 
            fig4, = plt.plot(x, y)


            # plt.legend([fig1, fig2,fig3,fig4], ["Chapter", "mean","mean+2sd","mean-2sd"])
            
            
            
            
            plt.ylabel( 'Linguistic Divercity' )
            plt.xlabel( 'Chapter' )
            plt.title(AO_sJBook)
            plt.grid(True)
            AO_sPlotFile = AO_sGraphsPass + str(AO_iJBook+1) + " " + AO_sJBook + ' 1 Linguistic Divercity.png'
            #print AO_sPlotFile
            plt.savefig(AO_sPlotFile)
            plt.close()

            if AO_l10erStart[0] > 0:
                shutil.copyfile(AO_sPlotFile,AO_s10ersGraphsPass + str(AO_iJBook+1) + " " + AO_sJBook + ' 1 Linguistic Divercity.png')





            #########################################
            # Graph 2
            #########################################
            
            if len(AO_lCommonWordUsage) > 1:
                AO_fSd = r.sd(AO_lCommonWordUsage[1:len(AO_lCommonWordUsage)])
            else:
                AO_fSd = 0
                
            AO_fMean = r.mean(AO_lCommonWordUsage[1:len(AO_lCommonWordUsage)])

            # if we leave it at 400 it will bdly effect the graph
            AO_lCommonWordUsage[0] = AO_fMean 


            # plot a triangle for each chapter's linguistic diversity
            # No 0 chapter 
            x = np.arange(1, len(AO_lCommonWordUsage)+1, 1);
            y = AO_lCommonWordUsage

            # Analyse the vecror for 10ers
            AO_l10erStart = AO_mNLTK.AO_lMTLookForLowPobabilirty(y,AO_sJBook,'Vocabulaty Commomality',AO_fMean,AO_s10ersFileName)

            if AO_l10erStart[0] > 0:
                fig10erA, = plt.plot([AO_l10erStart[0],AO_l10erStart[0]], [r.min(AO_lCommonWordUsage),r.max(AO_lCommonWordUsage)])
                fig10erB, = plt.plot([AO_l10erStart[1],AO_l10erStart[1]], [r.min(AO_lCommonWordUsage),r.max(AO_lCommonWordUsage)])

            # and Plot
            fig1, = plt.plot(x, y, 's')

            # plot a line at the mean
            for m in range (0, len(x)):
                y[m]=AO_fMean
            fig2, = plt.plot(x, y)


            # plot upper control  line at two standard deviations
            for m in range (0, len(x)):
                y[m]=2*AO_fSd + AO_fMean
            fig3, =plt.plot(x, y)

            #  plot lower control  line at two standard deviations
            for m in range (0, len(x)):
                y[m] = AO_fMean - 2*AO_fSd 
            fig4, = plt.plot(x, y)


            # plt.legend([fig1, fig2,fig3,fig4], ["Chapter", "mean","mean+2sd","mean-2sd"])
            
            
            
            plt.ylabel( 'Vocabulaty Commomality' )
            plt.xlabel( 'Chapter' )
            plt.title(AO_sJBook)
            plt.grid(True)
            AO_sPlotFile = AO_sGraphsPass + str(AO_iJBook+1) + " " + AO_sJBook + ' 2 Vocabulaty Commomality .png'
            plt.savefig(AO_sPlotFile)
            plt.close()

            if AO_l10erStart[0] > 0:
                shutil.copyfile(AO_sPlotFile,AO_s10ersGraphsPass + str(AO_iJBook+1) + " " + AO_sJBook + ' 2 Vocabulaty Commomality.png')






            #########################################
            # Graph 3
            #########################################


            # Build a word avarage vector#

            AO_sJBook = AO_tBooks[AO_iJBook][0]
            A0_iLastJBookChapter = AO_tBooks[AO_iJBook][2]
            AO_mJBookChapterXwords = AO_mBookLoader.AO_fLoadBook(AO_tBooks[AO_iJBook][0],
                                                                 AO_tBooks[AO_iJBook][1],
                                                                 AO_tBooks[AO_iJBook][2],
                                                                 AO_tBooks[AO_iJBook][3])

            # Clear the avarage word length per chapter in the book table
            for m in range (1, len(AO_lBookAvarageWordLegpgthByChapter)):
                n=AO_lBookAvarageWordLegpgthByChapter.pop(1)

            # for all the chapters in the J Bible
            for AO_iJChapter in range(1,A0_iLastJBookChapter +1):

                # clear the J list
                for m in range (1, len(AO_lJchapter)):
                    n=AO_lJchapter.pop(1)

                k = 1    
                # find the non zero length words in the j chapter
                while AO_mJBookChapterXwords[AO_iJChapter][k] > 0:
                    AO_lJchapter.append(int(AO_mJBookChapterXwords[AO_iJChapter][k]))
                    # print str(AO_iJChapter) + " " + str(AO_lJchapter[k-1])
                    k = k+1
                # end while
                    
                # call the R mean function to describe the J chapter.
                if len(AO_lJchapter) > 3:
                    AO_lBookAvarageWordLegpgthByChapter.append(r.mean(AO_lJchapter))
                    # print AO_lBookAvarageWordLegpgthByChapter
            # end for all of the chapters                                               
            # print AO_lBookAvarageWordLegpgthByChapter     
            # End of word length avarage vector#

            # print AO_lBookAvarageWordLegpgthByChapter

            # R does not like to avarage one element vectors
            if len(AO_lBookAvarageWordLegpgthByChapter) > 3:
                # print AO_lBookAvarageWordLegpgthByChapter 
                AO_fSd = r.sd(AO_lBookAvarageWordLegpgthByChapter[0:len(AO_lBookAvarageWordLegpgthByChapter)])
                AO_fMean = r.mean(AO_lBookAvarageWordLegpgthByChapter[0:len(AO_lBookAvarageWordLegpgthByChapter)])
            else:
                AO_fSd = 0
                AO_fMean = AO_lBookAvarageWordLegpgthByChapter[0]
            

            


            # if we leave it at 400 it will bdly effect the graph
            # AO_lCommonWordUsage[0] = AO_fMean 

            # plot a triangle for each chapter's linguistic diversity
            # No 0 chapter 
            x = np.arange(1, len(AO_lBookAvarageWordLegpgthByChapter)+1, 1);
            y = AO_lBookAvarageWordLegpgthByChapter

            # Analyse the vecror for 10ers
            AO_l10erStart = AO_mNLTK.AO_lMTLookForLowPobabilirty(y,AO_sJBook,'Avarege word Length',AO_fMean,AO_s10ersFileName)
            if AO_l10erStart[0] > 0:
                fig10erA, = plt.plot([AO_l10erStart[0],AO_l10erStart[0]], [r.min(AO_lBookAvarageWordLegpgthByChapter),r.max(AO_lBookAvarageWordLegpgthByChapter)])
                fig10erB, = plt.plot([AO_l10erStart[1],AO_l10erStart[1]], [r.min(AO_lBookAvarageWordLegpgthByChapter),r.max(AO_lBookAvarageWordLegpgthByChapter)])

                
                

            # and plot!
            fig1, = plt.plot(x, y, 'o')

            # plot a line at the mean
            for m in range (0, len(x)):
                y[m]=AO_fMean
            fig2, = plt.plot(x, y)


            # plot upper control  line at two standard deviations
            for m in range (0, len(x)):
                y[m]=2*AO_fSd + AO_fMean
            fig3, =plt.plot(x, y)

            #  plot lower control  line at two standard deviations
            for m in range (0, len(x)):
                y[m] = AO_fMean - 2*AO_fSd 
            fig4, = plt.plot(x, y)


            # plt.legend([fig1, fig2,fig3,fig4], ["Chapter", "mean","mean+2sd","mean-2sd"])
            
            
            
            plt.ylabel( 'Avarege word Length' )
            plt.xlabel( 'Chapter' )
            plt.title(AO_sJBook)
            plt.grid(True)
            AO_sPlotFile = AO_sGraphsPass + str(AO_iJBook+1) + " " + AO_sJBook + ' 3 Avarege word Length.png'
            plt.savefig(AO_sPlotFile)
            plt.close()

            if AO_l10erStart[0] > 0:
                shutil.copyfile(AO_sPlotFile,AO_s10ersGraphsPass + str(AO_iJBook+1) + " " + AO_sJBook + ' 3 Avarege word Length.png')


            #########################################
            # sub Graph 4
            #########################################

            AO_lLigusticDiversity = AO_mNLTK.AO_fNLP(AO_sJBook,AO_tBooks[AO_iJBook][1],A0_iLastJBookChapter,AO_tBooks[AO_iJBook][3])


            plt.figure(1)
            plt.subplot(311)

            if len(AO_lLigusticDiversity) > 1:
                AO_fSd = r.sd(AO_lLigusticDiversity)
            else:
                AO_fSd = 0
                
            AO_fMean = r.mean(AO_lLigusticDiversity)

            # plot a triangle for each chapter's linguistic diversity
            # No 0 chapter 
            x = np.arange(1, len(AO_lLigusticDiversity)+1, 1);
            y = AO_lLigusticDiversity
            fig1, = plt.plot(x, y, 'g^')

            # plot a line at the mean
            for m in range (0, len(x)):
                y[m]=AO_fMean
            fig2, = plt.plot(x, y)


            # plot upper control  line at two standard deviations
            for m in range (0, len(x)):
                y[m]=2*AO_fSd + AO_fMean
            fig3, =plt.plot(x, y)

            #  plot lower control  line at two standard deviations
            for m in range (0, len(x)):
                y[m] = AO_fMean - 2*AO_fSd 
            fig4, = plt.plot(x, y)


            # # plt.legend([fig1, fig2,fig3,fig4], ["Chapter", "mean","mean+2sd","mean-2sd"])
            
            plt.ylabel( 'Divercity' )
            # plt.xlabel( 'Chapter' )
            plt.title(AO_sJBook)
            plt.grid(True)
            # AO_sPlotFile = AO_sGraphsPass + AO_sJBook + ' 3 Linguistic Divercity.png'
            # plt.savefig(AO_sPlotFile)
            # plt.close()





            #########################################
            # Graph 5
            #########################################

            plt.subplot(312)

            # Build a word avarage vector#

            AO_sJBook = AO_tBooks[AO_iJBook][0]
            A0_iLastJBookChapter = AO_tBooks[AO_iJBook][2]
            AO_mJBookChapterXwords = AO_mBookLoader.AO_fLoadBook(AO_sJBook,AO_tBooks[AO_iJBook][1],A0_iLastJBookChapter,AO_tBooks[AO_iJBook][3])

            # Clear the avarage word length per chapter in the book table
            for m in range (1, len(AO_lBookAvarageWordLegpgthByChapter)):
                n=AO_lBookAvarageWordLegpgthByChapter.pop(1)

            # for all the chapters in the J Bible
            for AO_iJChapter in range(1,A0_iLastJBookChapter +1):

                # clear the J list
                for m in range (1, len(AO_lJchapter)):
                    n=AO_lJchapter.pop(1)

                k = 1    
                # find the non zero length words in the j chapter
                while AO_mJBookChapterXwords[AO_iJChapter][k] > 0:
                    AO_lJchapter.append(int(AO_mJBookChapterXwords[AO_iJChapter][k]))
                    k = k+1
                # end while
                    
                # call the R mean function to describe the J chapter. 
                AO_lBookAvarageWordLegpgthByChapter.append(r.mean(AO_lJchapter))
            # end for all of the chapters                                               
            # print AO_lBookAvarageWordLegpgthByChapter     
            # End of word length avarage vector#

            
            if len(AO_lBookAvarageWordLegpgthByChapter) > 1:
                AO_fSd = r.sd(AO_lBookAvarageWordLegpgthByChapter[0:len(AO_lBookAvarageWordLegpgthByChapter)])
            else:
                AO_fSd = 0
                
            AO_fMean = r.mean(AO_lBookAvarageWordLegpgthByChapter[0:len(AO_lBookAvarageWordLegpgthByChapter)])

            # if we leave it at 400 it will bdly effect the graph
            # AO_lCommonWordUsage[0] = AO_fMean 

            # plot a triangle for each chapter's linguistic diversity
            # No 0 chapter 
            x = np.arange(1, len(AO_lBookAvarageWordLegpgthByChapter)+1, 1);
            y = AO_lBookAvarageWordLegpgthByChapter
            fig1, = plt.plot(x, y, 'o')

            # plot a line at the mean
            for m in range (0, len(x)):
                y[m]=AO_fMean
            fig2, = plt.plot(x, y)


            # plot upper control  line at two standard deviations
            for m in range (0, len(x)):
                y[m]=2*AO_fSd + AO_fMean
            fig3, =plt.plot(x, y)

            #  plot lower control  line at two standard deviations
            for m in range (0, len(x)):
                y[m] = AO_fMean - 2*AO_fSd 
            fig4, = plt.plot(x, y)


            # # plt.legend([fig1, fig2,fig3,fig4], ["Chapter", "mean","mean+2sd","mean-2sd"])
            
            plt.ylabel( 'Length' )
            # plt.xlabel( 'Chapter' )
            # plt.title(AO_sJBook)
            plt.grid(True)
            #AO_sPlotFile = AO_sGraphsPass + str(AO_iJBook+1) + " " + AO_sJBook + ' 3 Avarege word Length.png'
            #plt.savefig(AO_sPlotFile)
            #plt.close()





            #########################################
            # sub Graph 6
            #########################################

            AO_lCommonWordUsage = AO_mPopularWords.AO_fPopularWords(AO_sJBook,AO_tBooks[AO_iJBook][1],A0_iLastJBookChapter,AO_tBooks[AO_iJBook][3])

            plt.subplot(313)

            if len(AO_lCommonWordUsage) > 1:
                AO_fSd = r.sd(AO_lCommonWordUsage[1:len(AO_lCommonWordUsage)])
            else:
                AO_fSd = 0
                
            AO_fMean = r.mean(AO_lCommonWordUsage[1:len(AO_lCommonWordUsage)])

            # if we leave it at 400 it will bdly effect the graph
            AO_lCommonWordUsage[0] = AO_fMean 

            # plot a triangle for each chapter's linguistic diversity
            # No 0 chapter 
            x = np.arange(1, len(AO_lCommonWordUsage)+1, 1);
            y = AO_lCommonWordUsage
            fig1, = plt.plot(x, y, 's')

            # plot a line at the mean
            for m in range (0, len(x)):
                y[m]=AO_fMean
            fig2, = plt.plot(x, y)


            # plot upper control  line at two standard deviations
            for m in range (0, len(x)):
                y[m]=2*AO_fSd + AO_fMean
            fig3, =plt.plot(x, y)

            #  plot lower control  line at two standard deviations
            for m in range (0, len(x)):
                y[m] = AO_fMean - 2*AO_fSd 
            fig4, = plt.plot(x, y)


            # # plt.legend([fig1, fig2,fig3,fig4], ["Chapter", "mean","mean+2sd","mean-2sd"])
            
            plt.ylabel( 'Commomality' )
            plt.xlabel( 'Chapter' )
            # plt.title(AO_sJBook)
            plt.grid(True)
            AO_sPlotFile = AO_sGraphsPass + str(AO_iJBook+1) + " " + AO_sJBook + ' 4-NLTK.png'
            plt.savefig(AO_sPlotFile)
            plt.close()

        
    # for all of the J Books
    
if __name__ == '__main__':
   
    main()
