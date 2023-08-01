"""
Prepare jdd badges input

BE AWARE THAT :
- CSV MUST CONTAINS COLUMNS 'Nom' AND 'Prénom'
- CANNOT PROCEED EXCEL FILES
"""
import pandas as pd
import os
from colorama import Fore, Style
from colorama import init as colorama_init
from sympy import *

colorama_init()
print(os.getcwd())

def create_file(input_file, output) :
    print(f"{Fore.BLUE}Creating badge file...{Style.RESET_ALL}")
    print(f'{Fore.BLUE}Formatting data .....{Style.RESET_ALL}')
    if ".csv" in input_file :
        df = pd.read_csv(input_file)
    else :
        raise IOError('File extension not supported. Must be .csv')
    df = df.sort_values(by="Nom")
    df['Nom'] = df['Nom'].apply(lambda x: x.title().strip())
    df['Prénom'] = df['Prénom'].apply(lambda x: x.title().strip())
    last_names = df['Nom'].to_list()
    first_names = df['Prénom'].to_list()
    list_combined = tuple(zip(last_names, first_names))
    print(f'{Fore.BLUE}Writing tex file .....{Style.RESET_ALL}')
    with open(output,'w') as file :
        for item in list_combined :
            file.write(r"\confpin{%s}{%s}" % item)
        print('Done')
    print(f"{Fore.GREEN}{Style.BRIGHT}File created under {output}{Style.RESET_ALL}")

def create_template(output):
    with open(output, 'w') as f :
        f.write(
            r""" 
%%%%
%
% ticket.sty example file for a pin for conferences
%
%%%%
% use the corresponding paper size for your ticket definition
\RequirePackage{fix-cm}
\documentclass[a4paper,10pt]{letter}

% Pou r le bold sc
\usepackage[T1]{fontenc} % To switch to the T1 encoding
\usepackage{kpfonts} % To switch to Latin Modern
\rmfamily % To load Latin Modern Roman and enable the following NFSS declarations.
% Declare that Latin Modern Roman (lmr) should take
% its bold (b) and bold extended (bx) weight, and small capital (sc) shape, 
% from the corresponding Computer Modern Roman (cmr) font, for the T1 font encoding.



% load ticket.sty with the appropriate ticket definition
\usepackage[freepin,boxed]{ticket}
\usepackage{calc}
\usepackage{minibox}
% load misc stuff
\usepackage{graphicx}
\usepackage{bold-extra}

\usepackage{pgfmath}
\unitlength=1mm
\newcommand{\badgeWidth}{86}
\newcommand{\badgeHeight}{54}

% Misc
\setlength{\fboxrule}{0pt} % Pas de bordure autour des framebox

\newcommand{\storeLengthInMM}[2]{%
  \FPdiv\result{#1}{2.83464} % Convert pt to mm
  \edef#2{\result}%
}
\makeatletter
\newcommand*{\getlength}[1]{\strip@mm#1}
\makeatother
% Taille du badge
\ticketSize{\badgeWidth}{\badgeHeight} % in unitlength
% Séparation du badge
\ticketDistance{0}{0} % in unitlength

% Taille en pt, pour les calculs
\newlength{\badgeWidthLength}
\newlength{\badgeHeightLength}
\setlength{\badgeWidthLength}{\badgeWidth mm}
\setlength{\badgeHeightLength}{\badgeHeight mm}

% V et H offset pour la bande de logo
\newcommand{\HOffsetLogo}{1} % Depuis les côtés du badges, présent des deux côtés
\newlength{\HOffsetLogoLength}
\setlength{\HOffsetLogoLength}{\HOffsetLogo mm}

\newcommand{\VOffsetLogo}{2} % Au dessus et en dessous des badges
\newlength{\VOffsetLogoLength}
\setlength{\VOffsetLogoLength}{\VOffsetLogo mm}
\newlength{\rescaledHeightLogos}
\newlength{\mmHeightLogo}

% Line H Offset
\newcommand{\lineOffset}{7}
% Texte titre du badge.
\newcommand{\jdddate}{\scriptsize Journées Des Doctorants <Date à modifier>} %Modifier ici la date
\newcommand{\jdddateVerticalOffset}{5} % Depuis le haut du badge
\newcommand{\jdddateverso}{\scriptsize École doctorale MIMME}

% Logo JDD
\newlength{\logoHeight}
\newlength{\rescaledWidthLogoJDD}
\newcommand{\logoHOffset}{0}

% Name
\newcommand{\nameHOffset}{5}
\newlength{\nameHOffsetLength}
\setlength{\nameHOffsetLength}{\nameHOffset mm}

% QR Code
\newcommand{\QRCodeHOffet}{2}
\newlength{\QRCodeWidthLength}

% Misc
\setlength{\rescaledHeightLogos}{\heightof{\includegraphics[width=\badgeWidthLength-\HOffsetLogoLength - \HOffsetLogoLength]{../../ressources/img/logos_labos}}}
\pgfmathsetmacro{\mmHeightLogo}{\rescaledHeightLogos/2.835+\VOffsetLogo}
\pgfmathsetmacro{\logoY}{\mmHeightLogo+\VOffsetLogo}  
\pgfmathsetmacro{\logoHeightNum}{\badgeHeight-\logoY-\jdddateVerticalOffset-\VOffsetLogo}
\setlength{\logoHeight}{\logoHeightNum mm}
\setlength{\rescaledWidthLogoJDD}{\widthof{\includegraphics[height=\logoHeight]{logoJDD}}}
\pgfmathsetmacro{\logoX}{\badgeWidth-\rescaledWidthLogoJDD/2.835-\QRCodeHOffet}

\setlength{\QRCodeWidthLength}{\widthof{\fbox{\includegraphics[height=\logoHeight]{qr_code_book_abstract}}}}
\pgfmathsetmacro{\QRx}{\QRCodeHOffet}
\pgfmathsetmacro{\QRxx}{\badgeWidth-\QRCodeWidthLength/2.835-\QRCodeHOffet}

% make your default ticket. \ticketdefault is somewhat like a background
\renewcommand{\ticketdefault}{%
    \put(0,\the\numexpr\badgeHeight-\jdddateVerticalOffset){\framebox[\badgeWidthLength][c]{\jdddate}}% Texte de  titre centré
    \put(\HOffsetLogo,\VOffsetLogo){\includegraphics[width=\badgeWidthLength-\HOffsetLogoLength - \HOffsetLogoLength]{logos_labos}}
    \put(\lineOffset,\mmHeightLogo){\line(1,0){\numexpr\badgeWidth-2*\lineOffset}}
    \put(\logoX,\logoY){\fbox{\includegraphics[height=\logoHeight]{example-image-a}}}%Mettre ici le chemin du logo voulu
}
\newlength{\textLengthName}
\pgfmathsetmacro{\textX}{0}
\pgfmathsetmacro{\textWidthName}{\badgeWidth-2*\nameHOffset-\rescaledWidthLogoJDD/2.835-\logoHOffset}
\setlength{\textLengthName}{\textWidthName mm}

\newlength{\textHeightLength}
% now what do you like to put in your ticket
\newcommand{\confpin}[2]{\ticket{%
    \put(\nameHOffset,\logoY){\fbox{\begin{minipage}[b][\logoHeight][c]{\textLengthName}\textbf{\Large\textsc{#1}\\\\#2}\end{minipage}}}%\huge\textsc{\textbf{#1}}\\\textbf{#2}
}
\renewcommand{\ticketdefault}{%
    \put(0,\the\numexpr\badgeHeight-\jdddateVerticalOffset){\framebox[\badgeWidthLength][c]{\jdddateverso}}% Texte de  titre centré
    \put(\HOffsetLogo,\VOffsetLogo){\includegraphics[width=\badgeWidthLength-\HOffsetLogoLength - \HOffsetLogoLength]{../../ressources/img/logos_labos}}
    \put(\lineOffset,\mmHeightLogo){\line(1,0){\numexpr\badgeWidth-2*\lineOffset}}
    \put(\QRx,\logoY){\fbox{\includegraphics[height=\logoHeight]{example-image-a}}}%Mettre un des deux QR CODE ici
    \put(\QRxx,\logoY){\fbox{\includegraphics[height=\logoHeight]{example-image-a}}}%Mettre un des deux QR CODE ici
}\ticket{}
\renewcommand{\ticketdefault}{%
    \put(0,\the\numexpr\badgeHeight-\jdddateVerticalOffset){\framebox[\badgeWidthLength][c]{\jdddate}}% Texte de  titre centré
    \put(\HOffsetLogo,\VOffsetLogo){\includegraphics[width=\badgeWidthLength-\HOffsetLogoLength - \HOffsetLogoLength]{../../ressources/img/logos_labos}}
    \put(\lineOffset,\mmHeightLogo){\line(1,0){\numexpr\badgeWidth-2*\lineOffset}}
    \put(\logoX,\logoY){\fbox{\includegraphics[height=\logoHeight]{example-image-a}}}
}
}

%% the pins for the partipiciants ... ;-)
%% you can generate this part from a database!
\begin{document}
\sffamily
\input{list_complete.tex}
\end{document}
""")
