#!/usr/bin/env python
# coding: utf-8

# ---
# ## Sorbonne Université
# # <center> Mathématiques discrètes </center>
# ## <center> LU2IN005 </center>
# ## <div style="text-align:right;"> Année 2022-2023 </div>
# ---

# ---
# # <center> TME programmation d'automates finis </center>
# L'objectif de ce TME est de programmer en python quelques uns des
# algorithmes pour les automates finis vus en cours et en TD, en
# utilisant des structures de données fournies dans le code mis à votre
# disposition.
# ---
# # Consignes
# Copiez dans votre répertoire de travail les fichiers présents dans le Dossier 
# *Fichiers Python fournis* de la page Moodle de l'UE.
# 
# Ils contiennent les définitions de structures de données décrites
# ci-dessous, ainsi que des aide-mémoire sur l'utilisation de python.
# 
# **Le seul fichier que vous êtes autorisés à modifier** est celui-ci, c'est-à-dire
# `automate_etudiant.ipynb`, partiellement prérempli. 
# Les instructions `return` sont à supprimer lorsque
# vous remplirez le contenu des différentes fonctions.  Les autres
# fichiers n'ont pas besoin d'être lus (mais ils peuvent l'être).
# Si votre programme nécessite de lire des fichiers, **ceux-ci doivent être enregistrés dans le répertoire ExemplesAutomates** que vous avez téléchargé.
# ---

# _Binôme_
# ----------
# 
# **NOM**:         ESSALEH              
# 
# **Prénom**:       ACHRAF         
# 
# **Numéro d'étudiant**:       21118166
# 
# **NOM**:
# 
# **Prénom**:   
# 
# **Numéro d'étudiant**: 
# 
# 

# ### Table des matières
# 
# > [1. Présentation](#sec1)
# >> [1.1 La classe `State`](#sec1_1) <br>
# >> [1.2 La classe `Transition`](#sec1_2) <br>
# >> [1.3 La classe `Automate`](#sec1_3)
# 
# > [2. Prise en mains](#sec2)
# >> [2.1 Création d'automates](#sec2_1) <br>
# >> [2.2 Premières manipulations](#sec2_2) <br>
# 
# > [3. Exercices de base : tests et complétion](#sec3)
# 
# > [4. Déterminisation](#sec4)
# 
# > [5. Constructions sur les automates réalisant des opérations sur les langages acceptés](#sec5)
# >> [5.1 Opérations ensemblistes sur les langages](#sec5_1) <br>
# >> [5.2 Opérations rationnelles sur les langages](#sec5_2)

# In[1]:


## Import des bibliothèques nécessaires au projet.
## Ne pas modifier les fichiers "bibliothèque".

## Interpréter cette cellule avant de continuer.

from transition import *
from state import *
import os
import copy
from automateBase import AutomateBase

class Automate(AutomateBase):
    pass


# ### 1. Présentation  <a class="anchor" id="sec1"></a>
# 
# Le projet utilise le langage python avec une syntaxe légèrement
# différente de celle vue en **LU1IN001 / 011**, parce qu'il exploite en particulier
# la notion de classes d'objets. Une introduction à cette notion est présentée dans le livre associé
# au cours : cf [Chapitre 13](https://www-licence.ufr-info-p6.jussieu.fr/lmd/licence/2021/ue/LU1IN001-2021oct/cours2020.pdf).
# 
# De plus, le typage des variables est noté de façon légèrement différente, en commentaires, pour les déclarations
# comme pour les arguments des fonctions. Pour ces derniers, les types sont indiqués dans la première ligne de la documentation de la fonction.
# 
# Les particularités sont brièvement expliquées en annexe
# de ce document. Par ailleurs, vous trouverez dans la section
# `projet` de la page Moodle un mémo sur la syntaxe python, ainsi que la carte de
# référence du langage utilisée en **LU1IN001 / 011**.  On rappelle qu'une ligne
# commençant par `#` est un commentaire, ignoré par
# l'interpréteur.
# 
# Toutes les structures de données nécessaires à la construction des
# automates sont fournies sous la forme de classes python, pour les
# transitions d'un automate, ses états, et les automates
# eux-mêmes. Cette section indique comment les utiliser.

# #### 1.1 La classe `State` <a class="anchor" id="sec1_1"></a>
# 
# Un état est représenté par
# - un entier `id` (type `int`) qui définit son identifiant,
# - un booléen `init` (type `bool`) indiquant si c'est un état initial,
# - un booléen `fin` (type `bool`) indiquant si c'est un état final,
# - une chaîne de caractères `label` (type `str`) qui définit son étiquette, permettant de le *décorer*. Par défaut, cette variable est la version chaîne de caractères de l'identifiant de l'état. 
# 
# On définit l'alias de type `State` pour représenter les variables de ce type. 
# 
# Ainsi, l'instruction ci-dessous crée une variable `s` représentant un état d'identifiant `1`, qui est un état initial mais pas final, dont l'identifiant et l'étiquette  `1` :

# In[2]:


# s : State
s = State(1, True, False)


# Si l'on souhaite avoir une étiquette différente de l'identifiant, on
# utilise un quatrième argument :

# In[3]:


s = State(1, True, False, 'etat 1') 


# On accède ensuite aux différents champs de `s` par la notation pointée : exécutez les cellules suivantes pour observer l'affichage obtenu.

# In[4]:


print('La valeur de s.id est : ')
print(s.id)


# In[5]:


print('La valeur de s.init est : ')
print(s.init)


# In[6]:


print('La valeur de s.fin est : ')
print(s.fin)


# In[7]:


print('La valeur de s.label est : ')
print(s.label)


# In[8]:


print("L'affichage de s est : ")
print(s)


# Ainsi, une variable de type `State` est affichée par son étiquette et, entre parenthèses, si c'est un état initial et/ou final.

# #### 1.2 La classe `Transition` <a class="anchor" id="sec1_2"></a>
# 
# Une transition est représentée par 
# - un état `stateSrc` (type `State`) correspondant à son état de départ
# - un caractère `etiquette` (type `str`) donnant son   étiquette
# - un état `stateDest` (type `State`) correspondant à son état de destination
# 
# On définit l'alias de type `Transition` pour représenter les variables de ce type.
# 
# La séquence d'instructions suivante crée la transition d'étiquette `"a"` de l'état `s` (défini ci-dessus) vers lui-même et affiche les différents champs de la transition :

# In[9]:


# t : Transition
t = Transition(s, "a", s)


# In[10]:


print('La valeur de t.etiquette est : ')
print(t.etiquette)


# In[11]:


print("L'affichage de t.stateSrc est : ")
print(t.stateSrc)


# On remarque que la variable `stateSrc` est de type `State`, on obtient donc un état, et non uniquement un
# identifiant d'état. 

# In[12]:


print("L'affichage de t.stateDest est : ")
print(t.stateDest)


# In[13]:


print("L'affichage de t est : ")
print(t)


# #### 1.3 La classe `Automate` <a class="anchor" id="sec1_3"></a>
# 
# Un automate est représenté par
# - l'ensemble de ses transitions `allTransitions` (de type `set[Transition]`) 
# - l'ensemble de ses états `allStates` (de type `set[State]`)
# - une étiquette `label` (de type `str`) qui est éventuellement vide.
# 
# On définit l'alias de type `Automate` pour représenter les variables de ce type.
# 
# Ainsi, de même que pour les classes précédentes, l'accès aux
# différents champs se fait par la notation pointée. Par exemple, on
# obtient l'ensemble des états d'un automate `monAutomate` par
# l'instruction `monAutomate.allStates`.
# 
# Pour créer un automate, il existe trois possibilités.

# **Création à partir d'un ensemble de transitions.**<br>
# On peut d'abord utiliser le constructeur de signature `Automate : set[Transition] -> Automate`.<br>
# Il déduit alors l'ensemble des états à partir de l'ensemble des transitions et définit par défaut l'étiquette
# de l'automate comme la chaîne de caractères vide.
# 
# Par exemple, en commençant par créer les états et les transitions nécessaires :

# In[14]:


## création d'états
# s1 : State
s1 = State(1, True, False)
# s2 : State
s2 = State(2, False, True)

## création de transitions
# t1 : Transition
t1 = Transition(s1,"a",s1)
# t2 : Transition
t2 = Transition(s1,"a",s2)
# t3 : Transition
t3 = Transition(s1,"b",s2)
# t4 : Transition
t4 = Transition(s2,"a",s2)
# t5 : Transition
t5 = Transition(s2,"b",s2)
# set_transitions : set[Transition]
set_transitions = {t1, t2, t3, t4, t5}

## création de l'automate
# aut : Automate
aut = Automate(set_transitions)


# L'affichage de cet automate, par la commande `print(aut)` produit alors le résultat suivant : 

# In[15]:


print(aut)


# Les états de l'automate sont déduits de l'ensemble de transitions.
# 
# Optionnellement, on peut donner un nom à l'automate, en utilisant la variable `label`, par exemple :

# In[16]:


# aut2 : Automate
aut2 = Automate(set_transitions, label="A") 

print(aut2)


# **Création à partir d'un ensemble de transitions et d'un ensemble d'états.**<br>
# Dans le second cas, on crée un automate à partir d'un ensemble de
# transitions mais aussi d'un ensemble d'états, par exemple pour représenter des
# automates contenant des états isolés. Pour cela, on utilise le
# constructeur `Automate : set[Transition] x set[State] -> Automate`.
# 
# On peut également, optionnellement, donner un nom à l'automate :

# In[17]:


# set_etats : set[State]
set_etats = {s1, s2}

# aut3 : Automate
aut3 = Automate(set_transitions, set_etats, "B")

print(aut3)


# L'ordre des paramètres peut ne pas être respecté **à la condition** que l'on donne leur nom explicitement. Ainsi, la ligne suivante est correcte :

# In[18]:


aut = Automate(setStates = set_etats, label = "A", setTransitions = set_transitions)

print(aut)


# **Création à partir d'un fichier contenant sa description.**<br>
# La fonction `Automate.creationAutomate : str -> Automate` prend en argument un nom de fichier qui décrit un automate et construit l'automate correspondant (voir exemple ci-dessous).
# 
# La description textuelle de l'automate doit suivre le format suivant (voir exemple ci-dessous) :
# - #E: suivi de la liste des noms des états, séparés par
#   des espaces ou des passages à la ligne. Les noms d'états peuvent
#   être n'importe quelle chaîne alphanumérique pouvant également
#   contenir le symbole `_`. Par contre, si le nom d'état
#   contient des symboles *non numériques* il ne doit pas commencer
#   par un chiffre, sous peine de provoquer une erreur à l'affichage.
#   Ainsi, `10` et `A1` sont des noms d'états possibles,
#   mais `1A` ne l'est pas.
# - #I: suivi de la liste des états initiaux
#   séparés par des espaces ou des passages à la ligne, 
# - #F: suivi de la liste des
#   états finaux séparés par des espaces ou des passages à la ligne, 
# - #T: suivi de la liste des transitions séparées par des
#   espaces ou des passages à la ligne. Chaque transition est donnée
#   sous le format `(etat1, lettre, etat2)`.
# 
# Par exemple le fichier `exempleAutomate.txt` contenant <br>
# `#E: 0 1 2 3`<br>
# `#I: 0`<br>
# `#F: 3`<br>
# `#T: (0 a 0)`<br>
# `	(0 b 0)`<br>
# `	(0 a 1)`<br>
# `	(1 a 2)`<br>
# `	(2 a 3)`<br>
# `	(3 a 3)`<br>
# `	(3 b 3)`<br>
# est formaté correctement. L'appel suivant produira l'affichage...

# In[19]:


# automate : Automate
automate = Automate.creationAutomate("ExemplesAutomates/exempleAutomate.txt")
print(automate)


# **Fonctions de manipulation des automates.**<br>
# La classe automate contient également de nombreuses fonctions utiles. Elles
# s'appliquent à un objet de type `Automate` et s'utilisent donc sous la forme
# `aut.<`*fonction*`>(<`*parametres*`>)` où `aut` est une variable de type `Automate`.
# 

# - `show : float -> NoneType` <br> 
#     prend en argument facultatif un flottant (facteur de grossissement, par défaut il vaut 1.0) et produit une représentation graphique de l'automate.<br>
#     Ainsi, en utilisant l'automate défini dans le fichier d'exemple précédent, l'instruction `automate.show(1.2)` produit l'image suivante :

# In[20]:


automate.show(1.2)


# - `addTransition : Transition -> bool`<br>
#   prend en argument une transition `t`, fait la mise à jour de
#   l'automate en lui ajoutant `t` et ajoute les états impliqués
#   dans l'automate s'ils en sont absents. Elle rend `True` si l'ajout a
#   eu lieu, `False` sinon (si `t` était déjà présente dans l'automate).
#   
# - `removeTransition : Transition -> bool`<br>
#   prend en argument une transition `t` et fait la mise à jour de
#   l'automate en lui enlevant la transition, sans modifier les
#   états. Elle rend `True` si la suppression a eu lieu, `False` sinon (si
#   `t` était absente de l'automate).
# 
# - `addState : State -> bool`<br>
#   prend en argument un état `s` et fait la mise à jour de
#   l'automate en lui ajoutant `s`.  Elle rend `True` si l'ajout a eu
#   lieu, `False` sinon (si `s` était déjà présent dans l'automate).
# 
# - `nextId : -> int`<br>
#   renvoie un entier id frais, en choisissant l'entier le plus petit,
#   strictement supérieur à tous les id des états de l'automate.
# 
# - `removeState : State -> bool`<br>
#   prend en argument un état `s` et fait la mise à jour de
#   l'automate en supprimant `s` ainsi que toutes ses transitions
#   entrantes et sortantes.  Elle rend `True` si l'ajout a eu lieu, `False`
#   sinon (si `s` était absent de l'automate).
#   
# - `getSetInitialStates :  -> set[State]`<br> 
#   rend l'ensemble des états initiaux.
# 
# - `getSetFinalStates :  -> set[State]`<br>
#   rend l'ensemble des états finaux.
# 
# - `getSetTransitionsFrom : State -> set[Transition]`<br>
#   rend l'ensemble des transitions sortant de l'état passé en argument.
# 
# - `prefixStates : int -> NoneType`<br>
#   modifie les identifiants et les étiquettes de tous les états de
#   l'automate en les préfixant par l'entier passé en argument.
# 
# - `succElem : State x str -> set[State]`<br>
#   étant donné un état `s` et un caractère `a`, elle rend l'ensemble des
#   états successeurs de `s` par le caractère `a`.  Formellement,
#   
#   $$succElem(s, a) = \{s' \in S \mid  s \xrightarrow{a} s'\}.$$
#   
#   Cet ensemble peut contenir plusieurs états si l'automate n'est pas déterministe.

# In[21]:


# Voilà le code de succElem

def succElem(self, state, lettre):
    """ State x str -> set[State]
        rend l'ensemble des états accessibles à partir d'un état state par l'étiquette lettre
    """
    successeurs = set()
    # t: Transitions
    for t in self.getSetTransitionsFrom(state):
        if t.etiquette == lettre:
            successeurs.add(t.stateDest)
    return successeurs

Automate.succElem = succElem


# Avec l'exemple précédent, on obtient :

# In[22]:


s0 = list(automate.getSetInitialStates())[0] ## on récupère l'état initial de automate
automate.succElem(s0, 'a')


# ### 2. Prise en mains  <a class="anchor" id="sec2"></a>
# 
# #### 2.1 Création d'automates <a class="anchor" id="sec2_1"></a>
# 
# Soit l'automate $\mathcal{A}$ défini sur l'alphabet $\{ a,b \}$, d'états $0,1,2$, 
# d'état initial 0, d'état final 2 et de transitions : <br>$(0,a,0)$, $(0,b,1)$, 
# $(1,a,2)$, $(1,b,2)$, $(2,a,0)$ et $(2,b,1)$.
# 
# 1. Créer l'automate $\mathcal{A}$ à l'aide de son ensemble de transitions. Pour cela, créer un état `s0`  
# d'identifiant $0$
#   qui soit initial, un état `s1` d'identifiant $1$ et un état
#   `s2` d'identifiant $2$ qui soit final. Puis créer `t1`, `t2`, `t3`, `t4`, `t5` et
#   `t6` les 6 transitions de l'automate. Créer enfin l'automate
#   `auto` à partir de ses transitions, par exemple avec l'appel<br>
#   `auto = Automate({t1,t2,t3,t4,t5,t6})`.<br>
#   Vérifier que l'automate correspond bien à $\mathcal{A}$ en l'affichant.

# In[23]:


s0 = State(0, True, False)
s1 = State(1, False, False)
s2 = State(2, False, True)
t1 = Transition(s0, "a", s0)
t2 = Transition(s0, "b", s1)
t3 = Transition(s1, "a", s2)
t4 = Transition(s1, "b", s2)
t5 = Transition(s2, "a", s0)
t6 = Transition(s2, "b", s1)
auto = Automate({t1, t2, t3, t4, t5, t6})
print(auto)
auto.show()


# 2. Créer l'automate $\mathcal{A}$ à l'aide de sa liste de
#   transitions et d'états, par exemple à l'aide de l'appel<br>
#   `auto1 = Automate({t1,t2,t3,t4,t5,t6}, {s0,s1,s2})`<br>
#   puis afficher l'automate obtenu à l'aide de `print` puis à l'aide de `show`.
#   Vérifier que l'automate `auto1` est bien
#   identique à l'automate `auto`.

# In[24]:


auto1 = Automate({t1, t2, t3, t4, t5, t6}, {s0, s1, s2})
print(auto1)
auto1.show()
#il est bien identique!!


# 3. Créer l'automate $\mathcal{A}$ à partir d'un fichier. Pour cela,
#   créer un fichier `auto2.txt`, dans lequel sont indiqués les
#   listes des états et des transitions, ainsi que l'état initial et
#   l'état final, en respectant la syntaxe donnée dans la section
#   précédente. Par exemple la liste d'états est décrite par la ligne
#   `#E: 0 1 2`.  Utiliser ensuite par exemple l'appel
#   `auto2 = Automate.creationAutomate("ExemplesAutomates/auto2.txt")`, puis afficher
#   l'automate `auto2` à l'aide de `print` ainsi qu'à l'aide de `show`.

# In[25]:


auto2 = Automate.creationAutomate("ExemplesAutomates/auto2.txt")
print(auto2)
auto2.show()


# #### 2.2 Premières manipulations <a class="anchor" id="sec2_2"></a>
# 
# 1. Appeler la fonction `removeTransition` sur l'automate
#   `auto` en lui donnant en argument la transition $(0,a,1)$. Il
#   s'agit donc de créer une variable `t` de type
#   `Transition` représentant $(0,a,1)$ et d'effectuer l'appel
#   `auto.removeTransition(t)`. Observer le résultat sur un
#   affichage.  Appeler ensuite cette fonction sur `auto` en lui
#   donnant en argument la transition `t1`. Observer le résultat
#   sur un affichage. Appeler la fonction `addTransition` sur
#   l'automate `auto` en lui donnant en argument la transition
#   `t1`. Vérifier que l'automate obtenu est bien le même
#   qu'initialement.

# In[26]:


t = Transition(s0, "a", s1)
auto.removeTransition(t)
print(auto)
auto.show()


# In[27]:


auto.removeTransition(t1)
print(auto)
auto.show()


# In[28]:


auto.addTransition(t1)
print(auto)
auto.show()


# 2. Appeler la fonction `removeState` sur l'automate
#   `auto` en lui donnant en argument l'état
#   `s1`. Observer le résultat. Appeler la fonction
#   `addState` sur l'automate `auto` en lui donnant en
#   argument l'état `s1`. Créer un état `s0bis` d'identifiant
#   $0$ et initial. Appeler la fonction `addState` sur
#   `auto` avec `s0bis` comme argument. Observer le résultat.

# In[29]:


auto.removeState(s1)
print(auto)
auto.show()


# In[30]:


s0bis = State(0, True, False)
auto.addState(s0bis)
print(auto)
auto.show()


# 3. Appeler la fonction `getSetTransitionsFrom` sur
#   l'automate `auto1` avec `s1` comme argument. Afficher
#   le résultat.

# In[31]:


auto1.getSetTransitionsFrom(s1)


# ### 3. Exercices de base : tests et complétion  <a class="anchor" id="sec3"></a>

# 1. Donner une définition de la fonction `succ`
#   qui, étant donné un ensemble d'états $S$ et une chaîne de caractères
#       $a$ (de longueur 1), renvoie l'ensemble des états successeurs de tous les états de $L$ par le caractère $a$. Cette fonction doit généraliser la fonction `succElem` pour qu'elle prenne en paramètre un ensemble d'états au lieu d'un seul état.  Formellement, si $S$ est un ensemble d'états et $a$ une lettre,
#   $$succ(S,a) = \bigcup_{s \in S}succ(s,a) = \{s' \in S \mid \mbox{il
#     existe } s \in L \mbox{ tel que } s \xrightarrow{a} s'\}.$$

# In[32]:




def succ(self, setStates, lettre):
    """ Automate x set[State] x str -> set[State]
        rend l'ensemble des états accessibles à partir de l'ensemble d'états setStates par l'étiquette lettre
    """
    s = set()
    for state in setStates:
        s = s.union(self.succElem(state, lettre))
    return s

Automate.succ = succ


# In[33]:


# On a défini auparavant un automate auto1, voilà les résultats le concernant, puis un jeu de tests :

auto1.show()
print('---')
assert auto1.succ({s0, s2}, 'b') == {s1}
assert auto1.succ({s0}, 'a') == {s0}
assert auto1.succ({s0, s1}, 'a') == {s0, s2}


# In[34]:


# Fournir un autre jeu de tests


# In[35]:


auto.show()
print('---')
assert auto1.succ({s1, s2}, 'b') == {s1, s2}
assert auto1.succ({s1}, 'a') == {s2}


# 2. Donner une définition de la fonction `accepte`
#   qui, étant donné une chaîne de caractères `mot`,
#   renvoie un booléen qui vaut vrai si et seulement si `mot` est accepté par l'automate. Attention, noter que l'automate peut ne pas être déterministe.

# In[36]:


# je l'ai corrige apres la remarque que vous m'aviez donner dans la premiere soumision

def accepte(self, mot) :
    """ Automate x str -> bool
        rend True si auto accepte mot, False sinon
    """
    states = self.getSetInitialStates()
    if states == set():
        return False
    for lettre in mot:
        states = self.succ(states, lettre)
        if states == set():
            return False
    finals = self.getSetFinalStates()
    for st in states:
        if st in finals:
            return True
    return False

Automate.accepte = accepte


# In[37]:


# On a défini auparavant un automate auto1, voilà les résultats le concernant, puis un jeu de tests :

auto1.show()
print('---')
assert auto1.accepte('aa') == False
assert auto1.accepte('ab') == False
assert auto1.accepte('aba') == True


# In[38]:


# Fournir un autre jeu de tests


# In[39]:


auto.show()
print('---')
assert auto1.accepte('abba') == False
assert auto1.accepte('aaabb') == True


# 3. Donner une définition de la fonction `estComplet`
#     qui, étant donné un automate `auto` et un ensemble de caractères `Alphabet`
#     renvoie un booléen qui vaut vrai si et
#     seulement si `auto` est complet par rapport à l'alphabet.
#     
#     On n'effectuera pas la vérification sur les états non accessibles depuis les états initiaux.

# In[40]:


#ca fonctionne

def estComplet(self, Alphabet) :
    """ Automate x set[str] -> bool
        rend True si auto est complet pour les lettres de Alphabet, False sinon
        hyp : les éléments de Alphabet sont de longueur 1
    """
    states = self.allStates
    for a in Alphabet:
        for s in states:
            if(succElem(self,s,a)==set()):
                return False
    return True
       

Automate.estComplet = estComplet


# In[41]:


# On a défini auparavant un automate auto1, voilà les résultats le concernant, puis un jeu de tests :

auto1.show()
print('---')
assert auto1.estComplet({'a', 'b'}) == True
assert auto1.estComplet({'a', 'c', 'b'}) == False


# In[42]:


# Fournir un autre jeu de tests


# In[43]:


auto.show()
print('---')
assert auto.estComplet({'a', 'b'}) == False
assert auto.estComplet({'a'}) == True


# 4. Donner une définition de la fonction `estDeterministe`
# qui, étant donné un automate `auto`,
#  renvoie un booléen qui vaut vrai si et seulement si `auto` est déterministe.

# In[44]:


# je voulais verifier si y'a qu'un etat initiale mais elle ne veut pas marcher

def estDeterministe(self) :
    """ Automate -> bool
        rend True si auto est déterministe, False sinon
    """
    #if(len(self.getSetInitialStates())>1) :
    #   return False
    Alphabet = {t.etiquette for t in self.allTransitions}
    states = self.allStates
    for st in states:
        for lettre in Alphabet:
            if len(self.succElem(st, lettre)) > 1:
                return False
    return True
    
Automate.estDeterministe = estDeterministe


# L'appel de fonction `copy.deepcopy(auto)` renvoie un nouvel automate identique à `auto`.

# In[45]:


# On a défini auparavant un automate auto1, voilà les résultats le concernant, puis un jeu de tests :

auto1.show()
print('---')
assert auto1.estDeterministe() == True

auto1bis = copy.deepcopy(auto1)
#t : Transition
t = Transition(s1, 'b', s0)
auto1bis.addTransition(t)
auto1bis.show()
print('---')
assert auto1bis.estDeterministe() == False

auto1bis.removeTransition(t)
auto1bis.show()
print('---')
assert auto1bis.estDeterministe() == True


# In[46]:


# Fournir un autre jeu de tests
#t = Transition(s0, 'a', s2)
#auto1bis.addTransition(t)
#auto1bis.show()
#print('---')
#assert auto1bis.estDeterministe() == False


# In[47]:


auto.show()
print('---')
assert auto.estDeterministe() == True

autobis = copy.deepcopy(auto)
t = Transition(s0, "a", s2)
autobis.addTransition(t)
autobis.show()
print('---')
assert autobis.estDeterministe() == False

autobis.removeTransition(t)
autobis.show()
print('---')
assert autobis.estDeterministe() == True


# 5. Donner une définition de la fonction `completeAutomate`
# qui, étant donné un automate `auto` et l'ensemble alphabet d'entrée `Alphabet`,
# renvoie l'automate complété d'`auto`.
#   
# Attention, il ne faut pas modifier `auto`, mais construire un nouvel automate.
# <br>Il pourra être intéressant d'utiliser l'appel de fonction
# `copy.deepcopy(auto)` qui renvoie un nouvel automate identique à `auto`.
# <br>On pourra faire appel à la fonction `nextId` afin de construire l'état $\bot$.

# In[48]:


# completer un automate

def completeAutomate(self, Alphabet) :
    """ Automate x str -> Automate
        rend l'automate complété de self, par rapport à Alphabet
    """  
    complete = copy.deepcopy(self)
    if self.estComplet(Alphabet):
        return complete
    newstate = State(self.nextId(), False, False)
    complete.addState(newstate)
    
    states = self.allStates
    
    for st in states:
        for lettre in Alphabet:
            if self.succElem(st, lettre) == set():
                t = Transition(st, lettre, newstate)
                complete.addTransition(t)
                
    for lettre in Alphabet:
        complete.addTransition(Transition(newstate, lettre, newstate))
    
    return complete

Automate.completeAutomate = completeAutomate


# In[49]:


# On a défini auparavant un automate auto1, voilà les résultats le concernant :

auto1.show()
print('---')
assert auto1.estComplet({'a', 'b'}) == True
auto1complet = auto1.completeAutomate({'a', 'b'})
auto1complet.show()
assert auto1complet.estComplet({'a', 'b'}) == True

print('---')
assert auto1.estComplet({'a', 'b', 'c'}) == False
auto1complet = auto1.completeAutomate({'a', 'b', 'c'})
auto1complet.show()
assert auto1complet.estComplet({'a', 'b','c'}) == True


# In[50]:


# Fournir un autre jeu de tests


# In[51]:


auto.show()
print('---')
assert auto.estComplet({'a'}) == True
autocomplet = auto.completeAutomate({'a'})
autocomplet.show()
assert autocomplet.estComplet({'a'}) == True

print('---')
assert auto.estComplet({'a', 'b'}) == False
autocomplet = auto.completeAutomate({'a', 'b'})
autocomplet.show()
assert autocomplet.estComplet({'a', 'b'}) == True


# ### 4. Déterminisation  <a class="anchor" id="sec4"></a>

# 1. Donner une définition de la fonction `newLabel`
# qui, étant donné un ensemble d'états renvoie une *chaîne de caractères* représentant l'ensemble de tous les labels des états.
# Par exemple, l'appel de `newLabel` sur un ensemble de 3 états dont les labels sont `'1', '2', '3'` renvoie `'{1,2,3}'`
# 
# Afin d'être assuré que l'ordre de parcours de l'ensemble des états n'a pas d'importance, il sera nécessaire de trier par ordre alphabétique la liste des `label` des états. On pourra faire appel à `L.sort()` qui étant donné la liste `L` de chaînes de caractères, la trie en ordre alphabétique.

# In[52]:


# A faire

def newLabel(S):
    """ set[State] -> str
    """
    L = []
    for state in S:
        L.append(state.label)
    L.sort()
    chaine = "{"
    lng = len(L)
    for i in range(lng-1):
        chaine = chaine + L[i] + ","
    chaine = chaine + L[lng-1] + "}"
    return chaine


# In[53]:


# On a défini auparavant un automate auto1, voilà un test le concernant :

assert newLabel(auto1.allStates) == '{0,1,2}'


# In[54]:


# Fournir un autre jeu de tests


# In[55]:


assert newLabel(auto.allStates) == '{0,2}'


# La fonction suivante permet de déterminiser un automate. On remarque qu'un état peut servir de clé dans un dictionnaire.

# In[56]:


def determinisation(self) :
    """ Automate -> Automate
    rend l'automate déterminisé de self """
    # Ini : set[State]
    Ini = self.getSetInitialStates()
    # fin : bool
    fin = False
    # e : State
    for e in Ini:
        if e.fin:
            fin = True
    lab = newLabel(Ini)
    s = State(0, True, fin, lab)
    A = Automate(set())
    A.addState(s)
    Alphabet = {t.etiquette for t in self.allTransitions}
    Etats = dict()
    Etats[s] = Ini
    A.determinisation_etats(self, Alphabet, [s], 0, Etats, set())
    return A


# L'automate déterminisé est construit dans `A`. Pour cela la fonction récursive `determinisation_etats` modifie en place l'automate `A`, et prend en outre les paramètres suivants :
# - `auto`, qui est l'automate de départ à déterminiser
# - `Alphabet` qui contient l'ensemble des lettres étiquetant les transistions de l'automate de départ
# - `ListeEtatsATraiter` qui est la liste des états à ajouter et à traiter dans `A` au fur et à mesure que l'on progresse dans `auto`.
# - `i` qui est l'indice de l'état en cours de traitement (dans la liste `ListeEtatsATraiter`).
# - `Etats` qui est un dictionnaire dont les clés sont les états de `A` et les valeurs associées sont l'ensemble d'états issus de `auto` que cette clé représente.
# - `DejaVus` est l'ensemble des labels d'états de `A` déjà vus.

# In[57]:


# A faire 

def determinisation_etats(self, auto, Alphabet, ListeEtatsATraiter, i, Etats, DejaVus):
    """ Automate x Automate x set[str] x list[State] x int x dict[State : set[State]], set[str] -> NoneType
    """
    courant = ListeEtatsATraiter[i]
    if courant.label not in DejaVus:
        DejaVus.add(courant.label)
    for lettre in Alphabet:
        newstates = auto.succ(Etats[courant], lettre)
        newlab = newLabel(newstates)
        if newlab in DejaVus:
            for st in self.allStates:
                if st.label == newlab:
                    self.addTransition(Transition(courant, lettre, st))
        else:
            fin = False
            for e in newstates:
                if e.fin:
                    fin = True
            s = State(self.nextId(), False, fin, newlab)
            self.addState(s)
            self.addTransition(Transition(courant, lettre, s))
            Etats[s] = newstates
            ListeEtatsATraiter.append(s)
            DejaVus.add(newlab)
    if (i + 1) < len(ListeEtatsATraiter):
        return determinisation_etats(self, auto, Alphabet, ListeEtatsATraiter, i+1, Etats, DejaVus)
            

Automate.determinisation_etats = determinisation_etats
Automate.determinisation = determinisation


# In[58]:


# Voici un test
#automate est l'automate construit plus haut a partir du fichier exempleAutomate.txt
automate = Automate.creationAutomate("ExemplesAutomates/exempleAutomate.txt")
automate.show()
auto_det = automate.determinisation()
print(auto_det.estDeterministe())
auto_det.show(2)


# In[59]:


#Fournir d'autres jeux de tests


# In[60]:


auto1.show()
print('---')
assert auto1.estDeterministe() == True

auto1bis = copy.deepcopy(auto1)
#t : Transition
t = Transition(s1, 'b', s0)
auto1bis.addTransition(t)
auto1bis.show()
print('---')
assert auto1bis.estDeterministe() == False

auto1bis_det = auto1bis.determinisation()
print(auto1bis_det.estDeterministe())
auto1bis_det.show()


# #J'ai pas pu faire la partie 5 je la ferai la seance de vendredi prochain

# ### 5. Constructions sur les automates réalisant  des opérations sur les langages acceptés <a class="anchor" id="sec5"></a>
# 
# 
# #### 5.1 Opérations ensemblistes sur les langages <a class="anchor" id="sec5_1"></a>
# 
# 1. Donner une définition de la fonction `complementaire` qui, étant donné un automate `auto` et un ensemble de caractères `Alphabet`, renvoie l'automate acceptant la langage complémentaire du langage accepté par `auto`. Ne pas modifier l'automate `auto`, mais construire un nouvel automate.

# In[61]:


#fonctionne

def complementaire(self, Alphabet):
    """ Automate -> Automate
        rend  l'automate acceptant pour langage le complémentaire du langage de self
    """
    det = self.determinisation()
    comp = det.completeAutomate(Alphabet)
    for state in comp.allStates:
        if state.fin:
            state.fin = False
        else:
            state.fin = True
    return comp

    

Automate.complementaire = complementaire   


# In[62]:


# Voici un test

automate = Automate.creationAutomate("ExemplesAutomates/exempleAutomate.txt")
automate.show()
Alphabet = {t.etiquette for t in automate.allTransitions}
auto_compl = automate.complementaire(Alphabet)
auto_compl.show(2)


# In[63]:


#Fournir d'autres tests


# In[64]:


auto1.show()
print('---')

Alphabet = {t.etiquette for t in auto1.allTransitions}
auto1_compl = auto1.complementaire(Alphabet)
auto1_compl.show()


# 2. Donner une définition de la fonction `intersection` qui, étant donné deux automates `auto1` et `auto2`, renvoie l'automate acceptant l'intersection des langages acceptés par `auto1` et `auto2`.
# 
# L'automate construit ne doit pas avoir d'état non accessible depuis l'état initial.

# In[65]:


#inter


def intersection(self, auto):
    """ Automate x Automate -> Automate
    rend l'automate acceptant pour langage l'intersection des langages des deux automates
    """
    Alphabet = {t.etiquette for t in self.allTransitions}
    inter = Automate(set())
    ListeEtatsATraiter = []
    i = 0
    Etats = dict()
    DejaVus = set()
    ini1 = self.getSetInitialStates()
    ini2 = auto.getSetInitialStates()
    for el1 in ini1:
        for el2 in ini2:
            fin = False
            if el1.fin and el2.fin:
                fin = True
            lab = "(" + el1.label + "," + el2.label + ")"
            DejaVus.add(lab)
            s = State(i, True, fin, lab)
            inter.addState(s)
            ListeEtatsATraiter.append(s)
            Etats[s] = [el1, el2]
            i = i + 1
    i = 0
    while i < len(ListeEtatsATraiter):
        courant = ListeEtatsATraiter[i]
        for lettre in Alphabet:
            sucs1 = self.succElem(Etats[courant][0], lettre)
            sucs2 = auto.succElem(Etats[courant][1], lettre)
            for el1 in sucs1:
                for el2 in sucs2:
                    fin = False
                    if el1.fin and el2.fin:
                        fin = True
                    lab = "(" + el1.label + "," + el2.label + ")"
                    if lab in DejaVus:
                        for state in inter.allStates:
                            if state.label == lab:
                                inter.addTransition(Transition(courant, lettre, state))
                    else:
                        DejaVus.add(lab)
                        s = State(inter.nextId(), False, fin, lab)
                        inter.addState(s)
                        inter.addTransition(Transition(courant, lettre, s))
                        ListeEtatsATraiter.append(s)
                        Etats[s] = [el1, el2]
        i = i + 1
        
    
            
    return inter
    
Automate.intersection = intersection


# In[66]:


#Un premier test

automate.show()
auto2.show()
inter = automate.intersection(auto2)
inter.show(2)


# In[67]:


# Fournir d'autres tests


# In[68]:


s1 = State(1, True, False, "1")
s2 = State(2, False, False, "2")
s3 = State(3, False, True, "3")
t1 = Transition(s1, "b", s1)
t2 = Transition(s1, "a", s2)
t3 = Transition(s2, "a", s2)
t4 = Transition(s2, "b", s3)
t5 = Transition(s3, "a", s3)
t6 = Transition(s3, "b", s3)
aut1 = Automate({t1, t2, t3, t4 , t5, t6})
aut1.show()

s4 = State(1, True, False, "1")
s5 = State(2, False, False, "2")
s6 = State(3, False, True, "3")
t7 = Transition(s4, "b", s5)
t8 = Transition(s5, "b", s5)
t9 = Transition(s5, "a", s6)
t10 = Transition(s6, "a", s6)
t11 = Transition(s6, "b", s5)
aut2 = Automate({t7, t8, t9, t10, t11})
aut2.show()

inter2 = aut1.intersection(aut2)
inter2.show(2)


# 3. (Question facultative) Donner une définition de la fonction `union` qui, étant donné deux automates `auto1` `auto2`, renvoie l'automate acceptant comme langage l'union des langages acceptés par `auto1` et `auto2`.

# In[69]:


#A faire par l'étudiant

def union (self, auto):
    """ Automate x Automate -> Automate
    rend l'automate acceptant pour langage l'union des langages des deux automates
    """
    Alphabet = {t.etiquette for t in self.allTransitions}
    uni = Automate(set())
    ListeEtatsATraiter = []
    i = 0
    Etats = dict()
    DejaVus = set()
    self_comp = self.completeAutomate(Alphabet)
    auto_comp = auto.completeAutomate(Alphabet)
    ini1 = self_comp.getSetInitialStates()
    ini2 = auto_comp.getSetInitialStates()
    for el1 in ini1:
        for el2 in ini2:
            fin = False
            if el1.fin or el2.fin:
                fin = True
            lab = "(" + el1.label + "," + el2.label + ")"
            DejaVus.add(lab)
            s = State(i, True, fin, lab)
            uni.addState(s)
            ListeEtatsATraiter.append(s)
            Etats[s] = [el1, el2]
            i = i + 1
    i = 0
    while i < len(ListeEtatsATraiter):
        courant = ListeEtatsATraiter[i]
        for lettre in Alphabet:
            sucs1 = self_comp.succElem(Etats[courant][0], lettre)
            sucs2 = auto_comp.succElem(Etats[courant][1], lettre)
            for el1 in sucs1:
                for el2 in sucs2:
                    fin = False
                    if el1.fin or el2.fin:
                        fin = True
                    lab = "(" + el1.label + "," + el2.label + ")"
                    if lab in DejaVus:
                        for state in uni.allStates:
                            if state.label == lab:
                                uni.addTransition(Transition(courant, lettre, state))
                    else:
                        DejaVus.add(lab)
                        s = State(uni.nextId(), False, fin, lab)
                        uni.addState(s)
                        uni.addTransition(Transition(courant, lettre, s))
                        ListeEtatsATraiter.append(s)
                        Etats[s] = [el1, el2]
        i = i + 1
        
    
            
    return uni


Automate.union = union  


# In[70]:


#Un premier test

automate.show()
auto2.show()
uni = automate.union(auto2)
uni.show(2)


# In[71]:


#Autre test


# In[72]:


s1 = State(1, True, False, "1")
s2 = State(2, False, False, "2")
s3 = State(3, False, True, "3")
t1 = Transition(s1, "b", s1)
t2 = Transition(s1, "a", s2)
t3 = Transition(s2, "a", s2)
t4 = Transition(s2, "b", s3)
t5 = Transition(s3, "a", s3)
t6 = Transition(s3, "b", s3)
aut1 = Automate({t1, t2, t3, t4 , t5, t6})
aut1.show()

s4 = State(1, True, False, "1")
s5 = State(2, False, False, "2")
s6 = State(3, False, True, "3")
t7 = Transition(s4, "b", s5)
t8 = Transition(s5, "b", s5)
t9 = Transition(s5, "a", s6)
t10 = Transition(s6, "a", s6)
t11 = Transition(s6, "b", s5)
aut2 = Automate({t7, t8, t9, t10, t11})
aut2.show()

aut1_comp = aut1.completeAutomate({'a', 'b'})
aut1_comp.show()
aut2_comp = aut2.completeAutomate({'a', 'b'})
aut2_comp.show()

uni2 = aut1.union(aut2)
uni2.show(2)


# #### 5.2 Opérations rationnelles sur les langages <a class="anchor" id="sec5_2"></a>
# 
# Programmer *une des deux* méthodes suivantes:
# 
# 1. Donner une définition de la fonction `concatenation` qui, étant donné deux automates `auto1` et `auto2`, renvoie l'automate acceptant comme langage la concaténation des langages acceptés par `auto1` et `auto2`.
# 
# 2. Donner une définition de la fonction `etoile` qui, étant donné un automate `auto`, renvoie l'automate acceptant comme langage l'étoile du langages accepté par `auto`.

# In[73]:


# conca
def concatenation (self, auto):
    """ Automate x Automate -> Automate
    rend l'automate acceptant pour langage la concaténation des langages des deux automates
    """
    self_cp = copy.deepcopy(self)
    auto_cp = copy.deepcopy(auto)
    ini1 = self_cp.getSetInitialStates()
    fin1 = self_cp.getSetFinalStates()
    sts1 = self_cp.allStates
    sts2 = auto_cp.allStates
    trs1 = self_cp.allTransitions
    trs2 = auto_cp.allTransitions
    b = True
    if(ini1.intersection(fin1)==set()):
        b = False
    concat = Automate(set())
    for state in sts1:
        concat.addState(state)
    ini2_new = set()
    for state in sts2:
        state.id = concat.nextId()
        if state.init:
            ini2_new.add(state)
        concat.addState(state)
    for tr in trs1:
        concat.addTransition(tr)
    for tr in trs2:
        concat.addTransition(tr)
    Alphabet = {t.etiquette for t in self.allTransitions}
    for state in concat.allStates:
        if state in sts1:
            for lettre in Alphabet:
                if (self_cp.succElem(state, lettre)).intersection(fin1) != set():
                    for el in ini2_new:
                        concat.addTransition(Transition(state, lettre, el))
    for state in concat.allStates:
        if state in fin1:
            state.fin = False
        if state in ini2_new and not b:
            state.init = False
    return concat
    


Automate.concatenation = concatenation


# In[74]:


#Un premier test

automate.show()
auto2.show()
concat = automate.concatenation(auto2)
concat.show(2)


# In[75]:


#Fournir un autre jeu de test


# In[76]:


s1 = State(0, True, False, "1")
s2 = State(1, False, False, "2")
s3 = State(2, False, True, "3")
t1 = Transition(s1, "a", s2)
t2 = Transition(s2, "b", s3)
t3 = Transition(s3, "a", s3)
t4 = Transition(s3, "b", s3)
aut1 = Automate({t1,t2,t3,t4})
aut1.show()

s5 = State(0, True, False, "A")
s6 = State(1, False, False, "B")
s7 = State(2, False, True, "C")
t5 = Transition(s5, "a", s5)
t6 = Transition(s5, "b", s5)
t7 = Transition(s5, "b", s6)
t8 = Transition(s6, "a", s7)
aut2 = Automate({t5,t6,t7,t8})
aut2.show()

concat2 = aut1.concatenation(aut2)
concat2.show(2)


# In[77]:


def etoile (self):
    """ Automate  -> Automate
    rend l'automate acceptant pour langage l'étoile du langage de a
    """
    self_cp = copy.deepcopy(self)
    sts = self_cp.allStates
    trs = self_cp.allTransitions
    ini = self_cp.getSetInitialStates()
    fin = self_cp.getSetFinalStates()
    etoile = Automate(set())
    for state in sts:
        etoile.addState(state)
    for tr in trs:
        etoile.addTransition(tr)
    Alphabet = {t.etiquette for t in self.allTransitions}
    for state in etoile.allStates:
        for lettre in Alphabet:
            if (self_cp.succElem(state, lettre)).intersection(fin) != set():
                for el in ini:
                    etoile.addTransition(Transition(state, lettre, el))
    newstate = State(etoile.nextId(), True, True)
    etoile.addState(newstate)
    return etoile

Automate.etoile = etoile


# In[78]:


#Un premier test

automate.show()
print("---")
autoetoile = automate.etoile()
autoetoile.show()


# In[79]:


#Fournir un autre jeu de tests


# In[80]:


s1 = State(1, True, False, "1")
s2 = State(2, False, False, "2")
s3 = State(3, False, True, "3")
t1 = Transition(s1, "b", s1)
t2 = Transition(s1, "a", s2)
t3 = Transition(s2, "b", s2)
t4 = Transition(s2, "a", s3)
t5 = Transition(s3, "b", s3)
aut = Automate({t1, t2, t3, t4, t5})
aut.show()
print("---")

aut_etoile = aut.etoile()
aut_etoile.show()


# In[ ]:




