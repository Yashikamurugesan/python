Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> data=pd.read_csv("f://DATA SCIENCE NOTES/pmk.csv",encoding='latin')
>>> data
       #      Position            Candidate  ... Turnout PMK Votes PMK Votes %
0          1         2         Annadurai. N  ...  85.50%    56,681      25.30%
1          2         2  Guru @ Gurunathan.J  ...  80.80%    52,738      26.10%
2          3         2    Sathiyamoorthy. A  ...  85.30%    61,521      29.70%
3          4         2    Anbumani Ramadoss  ...  87.30%    58,402      29.60%
4          5         3            Sekar K N  ...  63.40%    16,635       7.40%
..       ...       ...                  ...  ...     ...       ...         ...
225      226        11          Nagarajan B  ...  76.10%       490       0.30%
226      227        11          Hariharan R  ...  66.90%       398       0.30%
227      228        12          Shanmugam K  ...  84.10%       367       0.20%
228      229        13         Muniasamy A.  ...  81.10%       260       0.20%
229      230        13             Pandi. V  ...  68.30%       522       0.30%

[230 rows x 9 columns]
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 230 entries, 0 to 229
Data columns (total 9 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0     #             230 non-null    int64 
 1   Position        230 non-null    int64 
 2   Candidate       230 non-null    object
 3   AC Name         230 non-null    object
 4   Total Electors  230 non-null    object
 5   Total Votes     230 non-null    object
 6   Turnout         230 non-null    object
 7   PMK Votes       230 non-null    object
 8   PMK Votes %     230 non-null    object
dtypes: int64(2), object(7)
memory usage: 16.3+ KB
>>> data.shape
(230, 9)
>>> data.size
2070
>>> data.to_string()
'     \xa0\xa0#\xa0\xa0\xa0\xa0  Position                   Candidate                 AC Name Total Electors Total Votes Turnout PMK Votes PMK Votes %\n0          1         2                Annadurai. N                Edappadi       2,61,712    2,23,731  85.50%    56,681      25.30%\n1          2         2         Guru @ Gurunathan.J             Jayankondam       2,50,259    2,02,088  80.80%    52,738      26.10%\n2          3         2           Sathiyamoorthy. A        Pappireddippatti       2,43,140    2,07,287  85.30%    61,521      29.70%\n3          4         2           Anbumani Ramadoss              Pennagaram       2,26,254    1,97,554  87.30%    58,402      29.60%\n4          5         3                   Sekar K N                Ambattur       3,53,518    2,24,029  63.40%    16,635       7.40%\n5          6         3              Elavazagan K L               Anaikattu       2,28,249    1,80,385  79.00%    24,711      13.70%\n6          7         3                       Gopal                Anthiyur       2,05,788    1,68,035  81.70%    11,570       6.90%\n7          8         3                    Arpudham               Arakkonam       2,17,390    1,63,392  75.20%    20,130      12.30%\n8          9         3                 Rajasekar S                   Arani       2,55,752    2,07,796  81.20%    12,877       6.20%\n9         10         3                 G.Karikalan                   Arcot       2,44,127    2,01,388  82.50%    35,043      17.40%\n10        11         3                  Amsaveni G                   Attur       2,32,681    1,84,046  79.10%    18,363      10.00%\n11        12         3                     A.Kumar                  Bargur       2,26,603    1,86,674  82.40%    18,407       9.90%\n12        13         3              Ramanathan K V                 Bhavani       2,25,945    1,86,234  82.40%    20,727      11.10%\n13        14         3                  Ashokkumar             Bhuvanagiri       2,38,798    1,89,722  79.40%    33,681      17.80%\n14        15         3                  Arumugam.K            Chengalpattu       3,66,345    2,46,190  67.20%    20,899       8.50%\n15        16         3                  Murugan. C                 Chengam       2,48,143    2,09,000  84.20%    15,114       7.20%\n16        17         3                Srinivasan G                 Cheyyar       2,43,709    2,03,565  83.50%    37,491      18.40%\n17        18         3                      Arul R             Chidambaram       2,28,166    1,68,905  74.00%    24,226      14.30%\n18        19         3             Senthil. R. Dr.              Dharmapuri       2,50,333    2,05,225  82.00%    56,727      27.60%\n19        20         3         Shanmugavel Murty.A              Gangavalli       2,17,595    1,74,215  80.10%    10,715       6.20%\n20        21         3              Ganesh Kumar A                  Gingee       2,50,191    1,98,698  79.40%    28,515      14.40%\n21        22         3                    Deepa .B              Gudiyattam       2,60,612    1,92,747  74.00%     7,505       3.90%\n22        23         3                  Selvaraj M           Gummidipoondi       2,59,194    2,12,864  82.10%    43,055      20.20%\n23        24         3                 Ponnusamy.G                Jolarpet       2,22,146    1,79,601  80.80%    17,516       9.80%\n24        25         3                  Kalidass R            Kalasapakkam       2,18,565    1,84,349  84.30%    23,825      12.90%\n25        26         3             P. Magesh Kumar            Kancheepuram       2,96,751    2,20,467  74.30%    30,102      13.70%\n26        27         3               Shanmugam N T                 Katpadi       2,27,250    1,75,378  77.20%    12,728       7.30%\n27        28         3             Edirolimanian G            Kilpennathur       2,34,104    1,96,123  83.80%    20,737      10.60%\n28        29         3              Kusalakumari.C      Kilvaithinankuppam       2,04,298    1,63,236  79.90%    13,046       8.00%\n29        30         3                     Kumar.S             Krishnagiri       2,44,487    1,98,237  81.10%    15,736       7.90%\n30        31         3              Vaithilingam G                  Kunnam       2,54,896    2,02,020  79.30%    37,271      18.50%\n31        32         3             Muthukrishnan S             Kurinjipadi       2,21,868    1,86,664  84.10%    22,705      12.20%\n32        33         3                  Eraviraj G               Madavaram       3,97,265    2,64,427  66.60%    14,245       5.40%\n33        34         3               A.Adhikesavan            Madurantakam       2,19,928    1,76,354  80.20%    16,215       9.20%\n34        35         3             Rajashekaran Vr                  Mailam       2,10,950    1,69,489  80.30%    25,711      15.20%\n35        36         3                  Ayyappan.A          Mayiladuthurai       2,34,079    1,67,168  71.40%    13,115       7.90%\n36        37         3                    Mani.G.K                  Mettur       2,62,849    2,05,745  78.30%    49,939      24.30%\n37        38         3                Tamilarasu.A                  Omalur       2,66,164    2,25,556  84.70%    48,721      21.60%\n38        39         3                  Mannan. K.                Palacode       2,11,355    1,86,887  88.40%    31,612      16.90%\n39        40         3              Dharmalingam.A                 Panruti       2,26,590    1,83,477  81.00%    18,666      10.20%\n40        41         3                   Pandian A                 Ponneri       2,47,430    1,95,364  79.00%     9,586       4.90%\n41        42         3                 Anbalagan.R               Poompuhar       2,56,713    1,91,280  74.50%    16,241       8.50%\n42        43         3             Parthasarathy C             Poonamallee       3,09,083    2,36,722  76.60%    15,827       6.70%\n43        44         3                Murali. M. K                 Ranipet       2,46,310    1,88,621  76.60%    23,850      12.60%\n44        45         3              Pushpagandhi J               Rasipuram       2,22,650    1,84,074  82.70%     6,952       3.80%\n45        46         3         Kathir Raasaratinam           Salem (North)       2,67,624    1,87,811  70.20%     7,975       4.30%\n46        47         3                     Kumar K           Salem (South)       2,63,957    1,93,768  73.40%     6,325       3.30%\n47        48         3                      Arul.R            Salem (West)       2,70,641    1,99,371  73.70%    29,982      15.00%\n48        49         3                 Sivaraman S            Sankarapuram       2,51,971    2,02,263  80.30%    13,612       6.70%\n49        50         3                    Kannan.P                 Sankari       2,56,471    2,12,929  83.00%    37,927      17.80%\n50        51         3                 K.Saravanan               Sholingur       2,54,525    2,09,373  82.30%    50,827      24.30%\n51        52         3                  Ramkumar.K         Shozhinganallur       5,75,773    3,38,365  58.80%    15,595       4.60%\n52        53         3              Muthukumar.Pon                Sirkazhi       2,31,842    1,76,325  76.10%    14,890       8.40%\n53        54         3                Muthuraman.C           Sriperumbudur       3,00,120    2,33,186  77.70%    18,185       7.80%\n54        55         3                     Vasu. K              Thiruporur       2,50,050    1,99,025  79.60%    28,125      14.10%\n55        56         3                  Balayogi V             Thiruvallur       2,54,359    2,04,826  80.50%    31,935      15.60%\n56        57         3              Madahaiyan.R.S       Thiruvidaimarudur       2,33,519    1,83,030  78.40%    13,709       7.50%\n57        58         3                  Kalidoss A              Tindivanam       2,20,510    1,73,038  78.50%    29,848      17.30%\n58        59         3                  Balasakthi            Tirukkoyilur       2,38,318    1,86,328  78.20%    18,822      10.10%\n59        60         3                    Raja.T.K              Tirupattur       2,26,179    1,76,650  78.10%    12,227       6.90%\n60        61         3              Vaithilingam A               Tiruttani       2,73,887    2,20,333  80.40%    29,596      13.40%\n61        62         3                   Pandian L          Tiruvannamalai       2,55,353    2,02,022  79.10%     7,916       3.90%\n62        63         3                 T.N.Anguthi              Uthangarai       2,17,792    1,78,899  82.10%    23,500      13.10%\n63        64         3             Gangadharan.Pon             Uthiramerur       2,42,572    1,97,126  81.30%    24,221      12.30%\n64        65         3              Vadivelravanan               Vandavasi       2,23,241    1,79,055  80.20%    24,277      13.60%\n65        66         3                    Sankar P                   Vanur       2,20,293    1,72,998  78.50%    27,240      15.80%\n66        67         3                Samraj.A.R.B              Veerapandi       2,38,532    2,03,890  85.50%    17,218       8.40%\n67        68         3               Tamil Selvi M            Veppanahalli       2,26,937    1,91,843  84.50%     5,476       2.90%\n68        69         3                 Anbumani. C              Vikravandi       2,17,174    1,77,252  81.60%    41,428      23.40%\n69        70         3                 Palanivel P              Villupuram       2,45,110    1,87,263  76.40%    36,456      19.50%\n70        71         3            Tamizharasi P Dr            Vridhachalam       2,32,531    1,82,870  78.60%    29,340      16.00%\n71        72         3                    Selvam.R                 Yercaud       2,58,758    2,19,430  84.80%    17,998       8.20%\n72        73         4                 Arulmani .S                Alangudi       1,96,502    1,57,028  79.90%     5,514       3.50%\n73        74         4           Thirumavalavan. K                Ariyalur       2,47,475    2,09,182  84.50%    13,529       6.50%\n74        75         4            Anandakrishnan N                   Avadi       3,87,261    2,65,738  68.60%    12,428       4.70%\n75        76         4                 Sadaiyappan                 Cheyyur       2,11,135    1,67,307  79.20%    17,892      10.70%\n76        77         4        Thamaraikannan Pazha               Cuddalore       2,28,538    1,70,626  74.70%    16,905       9.90%\n77        78         4                     Agnes F  Dr.Radhakrishnan Nagar       2,55,198    1,71,142  67.10%     3,011       1.80%\n78        79         4                    S.Murali                   Harur       2,25,231    1,88,042  83.50%    27,747      14.80%\n79        80         4                   Muniraj P                   Hosur       2,96,779    2,11,786  71.40%    10,309       4.90%\n80        81         4            Senthamilselvi R            Kallakurichi       2,64,413    2,10,711  79.70%     9,736       4.60%\n81        82         4                 Sozhan.Anbu     Kattumannarkoil(SC)       2,10,687    1,64,161  77.90%    25,890      15.80%\n82        83         4                   Vanitha.A                Kilvelur       1,63,189    1,36,880  83.90%     2,637       1.90%\n83        84         4               K.Venkatraman              Kumbakonam       2,46,071    1,86,234  75.70%     8,048       4.30%\n84        85         4              Srinivasan N V             Maduravoyal       3,91,693    2,41,942  61.80%    17,328       7.20%\n85        86         4         Balasubramaniyan. S              Mannargudi       2,40,899    1,85,336  76.90%     1,983       1.10%\n86        87         4              Suresh Kumar N                Mylapore       2,57,032    1,52,344  59.30%     5,806       3.80%\n87        88         4               Elavarasan. E                Nannilam       2,53,096    2,01,972  79.80%     5,060       2.50%\n88        89         4                     Jagan K                 Neyveli       2,00,260    1,57,531  78.70%    19,749      12.50%\n89        90         4                Alayamani .G               Papanasam       2,38,119    1,80,637  75.90%     4,963       2.80%\n90        91         4             M.Sathiyaseelan              Perambalur       2,75,932    2,20,233  79.80%     4,222       1.90%\n91        92         4                Velayutham.A                   Polur       2,25,566    1,94,484  86.20%    17,184       8.80%\n92        93         4                 Pandiyan.Kp           Rishivandiyam       2,47,152    1,95,830  79.20%     8,148       4.20%\n93        94         4              Sahadevan.T.R.                Saidapet       2,79,207    1,64,477  58.90%     5,913       3.60%\n94        95         4                Arunrajan D.                  Thalli       2,28,512    1,86,900  81.80%     5,253       2.80%\n95        96         4               Vanithamani D       Thiru-Vi-Ka-Nagar       2,15,120    1,33,765  62.20%     2,056       1.50%\n96        97         4                Sivakumar .R              Thiruvarur       2,52,466    1,94,618  77.10%     1,787       0.90%\n97        98         4            Vasanthakumari.R           Thiruvottiyur       2,86,872    1,87,144  65.20%     4,025       2.20%\n98        99         4                  Archunan E          Tittagudi (SC)       2,06,909    1,58,219  76.50%    11,438       7.20%\n99       100         4                     Balu K.           Ulundurpettai       2,72,569    2,26,647  83.20%    20,233       8.90%\n100      101         4           Lakshmi Narayanan                 Vellore       2,47,628    1,68,879  68.20%     5,185       3.10%\n101      102         5               Srinivasan R.                 Alandur       3,41,623    2,12,270  62.10%     7,194       3.40%\n102      103         5                Akhilesh A M              Anna Nagar       2,85,165    1,68,933  59.20%     5,619       3.30%\n103      104         5                 Vadivel.N.R            Bhavanisagar       2,37,600    1,93,571  81.50%     1,485       0.80%\n104      105         5               A.V.A.Kassali  Chepauk-Thiruvallikeni       2,25,920    1,40,171  62.00%     2,511       1.80%\n105      106         5               Parasuraman R                Dindigul       2,47,238    1,82,636  73.90%     2,718       1.50%\n106      107         5                 Rajendran A                  Egmore       1,90,949    1,17,795  61.70%     1,814       1.50%\n107      108         5                     S.Gopal                Kolathur       2,61,913    1,64,754  62.90%     3,022       1.80%\n108      109         5            G. Ramachandiran              Kovilpatti       2,44,448    1,63,257  66.80%     1,075       0.70%\n109      110         5              Ravichandran A            Madathukulam       2,24,447    1,69,397  75.50%     2,443       1.40%\n110      111         5              Aasai Kumar R.           Madurai North       2,33,677    1,50,889  64.60%     2,039       1.40%\n111      112         5                   Ragavan S                  Musiri       2,11,512    1,68,424  79.60%     1,423       0.80%\n112      113         5                 Duraisamy E                Namakkal       2,43,892    1,90,613  78.20%     2,751       1.40%\n113      114         5                 Ramoorthy N             Nilakkottai       2,16,344    1,72,722  79.80%     2,201       1.30%\n114      115         5         Saravana Iyappan. M              Orathanadu       2,26,104    1,78,141  78.80%     1,444       0.80%\n115      116         5                Venkatesan R              Pallavaram       4,03,787    2,45,381  60.80%     9,339       3.80%\n116      117         5         M.Venkatesh Perumal                Perambur       2,88,901    1,85,514  64.20%     3,685       2.00%\n117      118         5                    Susila K          Senthamangalam       2,32,916    1,87,253  80.40%     2,447       1.30%\n118      119         5                    R Suresh                Tambaram       3,72,883    2,30,348  61.80%     7,631       3.30%\n119      120         5                Rajamohan. S       Thiruthuraipoondi       2,22,380    1,73,852  78.20%     2,005       1.20%\n120      121         5                 R.Kanakaraj            Thiruvaiyaru       2,48,188    2,01,043  81.00%     1,571       0.80%\n121      122         5                    Vinoth.V        Thiyagarayanagar       2,40,352    1,38,412  57.60%     5,071       3.70%\n122      123         5                    Rangan V         Thousand Lights       2,43,386    1,38,770  57.00%     3,968       2.90%\n123      124         5            Vijayaraghavan.K  Tiruchirappalli (West)       2,53,551    1,75,323  69.10%     1,780       1.00%\n124      125         5                   Balraj M.          Udhagamandalam       2,00,138    1,37,243  68.60%       781       0.60%\n125      126         5              Kirubakaran.R.             Vaniyambadi       2,23,883    1,70,864  76.30%     9,283       5.40%\n126      127         5                 Usha Kannan              Vedaranyam       1,81,787    1,45,597  80.10%     2,081       1.40%\n127      128         5            Vinoba Bhoopathy               Velachery       2,96,329    1,71,297  57.80%     6,809       4.00%\n128      129         5               V.Subramanian             Villivakkam       2,52,292    1,46,675  58.10%     4,193       2.90%\n129      130         5                C.H. Jayarao           Virugampakkam       2,86,046    1,67,442  58.50%     3,945       2.40%\n130      131         6                R. Anbalagan            Ambasamudram       2,33,876    1,69,487  72.50%     1,310       0.80%\n131      132         6                 Ameen Basha                   Ambur       2,10,433    1,59,443  75.80%     4,643       2.90%\n132      133         6              Aravindkumar.D           Aruppukkottai       2,04,976    1,62,400  79.20%       817       0.50%\n133      134         6     Nirmala Gnanasoundari I                  Athoor       2,69,948    2,27,147  84.10%       671       0.30%\n134      135         6             Kamaraj Natesan      Coimbatore (North)       3,02,353    1,84,308  61.00%     2,196       1.20%\n135      136         6                 Madhavan. K         Dharapuram (SC)       2,36,823    1,80,028  76.00%     1,515       0.80%\n136      137         6                    Arumugam            Erode (West)       2,55,003    1,85,964  72.90%     3,000       1.60%\n137      138         6     Murugesan @ Murugesh R.                 Gudalur       1,78,142    1,29,270  72.60%       684       0.50%\n138      139         6               Sureshkumar R                 Harbour       1,82,820    1,02,137  55.90%     1,011       1.00%\n139      140         6               Amirtavalli V                Kangayam       2,31,742    1,81,287  78.20%     1,544       0.90%\n140      141         6       Hilman Bruce Edwin. S           Kanniyakumari       2,81,262    2,08,354  74.10%       712       0.30%\n141      142         6               Thangavelu A.         Kavundampalayam       4,06,349    2,67,126  65.70%     2,533       1.00%\n142      143         6                 Alexander J               Killiyoor       2,49,258    1,52,131  61.00%       615       0.40%\n143      144         6                    Murthy S           Kumarapalayam       2,32,414    1,83,658  79.00%     2,773       1.50%\n144      145         6                   Alaguraja            Madurai East       2,86,211    2,11,227  73.80%     1,113       0.50%\n145      146         6              Krishnakumar R            Madurai West       2,79,424    1,81,421  64.90%       927       0.50%\n146      147         6                   Prince. M           Manachanallur       2,17,178    1,77,694  81.80%     1,212       0.70%\n147      148         6                  Moorthi. K           Mettuppalayam       2,73,728    2,07,353  75.80%     1,870       0.90%\n148      149         6                  Nachimuthu            Modakkurichi       2,21,957    1,73,953  78.40%     2,809       1.60%\n149      150         6                    Balraj.A            Nagapattinam       1,84,181    1,33,443  72.50%     1,036       0.80%\n150      151         6                 Seerangan K                  Natham       2,58,472    2,05,167  79.40%     1,155       0.60%\n151      152         6             Murugaperumal.R             Ottapidaram       2,17,224    1,57,784  72.60%     1,066       0.70%\n152      153         6                 Thangaraj.R              Paramakudi       2,46,166    1,67,411  68.00%       690       0.40%\n153      154         6                  Ramesh Pon         Paramathi-Velur       2,10,835    1,73,648  82.40%     3,740       2.20%\n154      155         6                  Lakshmi. C            Pattukkottai       2,26,518    1,64,349  72.60%     3,607       2.20%\n155      156         6                    Kannan.R             Periyakulam       2,58,145    1,90,735  73.90%     1,025       0.50%\n156      157         6                 Kumaresan.P              Perundurai       2,10,871    1,80,272  85.50%     1,498       0.80%\n157      158         6              Lakshmanan. P.             Rajapalayam       2,21,788    1,68,398  75.90%     1,073       0.60%\n158      159         6                  Muthaiah S             Sholavandan       2,06,777    1,64,394  79.50%       857       0.50%\n159      160         6           Ashok Jayendar P.             Singanallur       3,04,591    1,84,799  60.70%     2,865       1.60%\n160      161         6              Thilagabama M.                Sivakasi       2,34,432    1,72,998  73.80%     1,350       0.80%\n161      162         6             Umamaheshwari.S               Srirangam       2,81,063    2,21,279  78.70%     1,548       0.70%\n162      163         6                    Suresh A              Thirumayam       2,05,506    1,56,654  76.20%       950       0.60%\n163      164         6               Balamurugan K       Thiruparankundram       2,79,299    1,94,369  69.60%     1,237       0.60%\n164      165         6                Dilipkumar.K           Thiruverumbur       2,67,527    1,80,292  67.40%     1,498       0.80%\n165      166         6              Chinnadurai.M.            Thoothukkudi       2,75,218    1,86,311  67.70%     1,069       0.60%\n166      167         6  Kumara Gurupara Adithan D.             Tiruchendur       2,23,973    1,64,994  73.70%       578       0.40%\n167      168         6                 Sridhar .B.  Tiruchirappalli (East)       2,40,767    1,62,656  67.60%     1,866       1.20%\n168      169         6                 Duraisamy P          Udumalaipettai       2,50,547    1,79,611  71.70%     1,975       1.10%\n169      170         6             Ganeshperumal.P            Virudhunagar       2,05,887    1,50,512  73.10%       556       0.40%\n170      171         7               P.Gunasekaran               Alangulam       2,43,056    1,91,237  78.70%       674       0.40%\n171      172         7                      Ravi.K               Andipatti       2,52,747    1,96,700  77.80%       817       0.40%\n172      173         7               Marimuthu K K           Avanashi (SC)       2,48,719    1,90,528  76.60%     1,480       0.80%\n173      174         7             Palanychamy Ki.      Coimbatore (South)       2,42,869    1,50,202  61.80%     1,111       0.70%\n174      175         7         Alexanderrajkumar A                Colachel       2,60,607    1,65,612  63.50%       772       0.50%\n175      176         7           Pon. Katchikannan                  Cumbum       2,62,147    1,91,863  73.20%       763       0.40%\n176      177         7            Palanimanickam.M         Gandharvakottai       1,84,576    1,44,534  78.30%       530       0.40%\n177      178         7                   Kuppusamy       Gobichettipalayam       2,41,198    2,01,877  83.70%     1,045       0.50%\n178      179         7               Duraipandi Pr               Karaikudi       2,82,460    1,98,667  70.30%       897       0.50%\n179      180         7                Murugesan .M                   Karur       2,31,209    1,83,218  79.20%     1,376       0.80%\n180      181         7             Umamaheswaran R                 Lalgudi       2,01,236    1,64,601  81.80%       745       0.50%\n181      182         7                    Selvam T         Madurai Central       2,34,511    1,49,299  63.70%     1,007       0.70%\n182      183         7              Mari Selvam. S           Madurai South       2,20,259    1,43,693  65.20%       864       0.60%\n183      184         7           Leema Sivakumar A              Manapparai       2,61,856    2,02,592  77.40%       826       0.40%\n184      185         7             Nishthar Ali .S           Palayamkottai       2,54,284    1,51,701  59.70%     1,315       0.90%\n185      186         7                    Kumar. S                Palladam       3,25,238    2,34,062  72.00%     2,292       1.00%\n186      187         7                 Perumal T S               Royapuram       1,86,386    1,19,769  64.30%     2,126       1.80%\n187      188         7             Balakrishnan M.                  Sattur       2,22,271    1,74,484  78.50%       768       0.40%\n188      189         7               Rajasekaran.N               Sivaganga       2,71,108    1,87,812  69.30%     1,284       0.70%\n189      190         7                Ganesan P.K.                   Sulur       2,79,722    2,09,433  74.90%     1,687       0.80%\n190      191         7               Seetharaman P                 Tenkasi       2,61,504    1,99,384  76.20%     1,222       0.60%\n191      192         7                      Raja S            Tiruchengodu       2,18,127    1,74,285  79.90%     2,012       1.20%\n192      193         7              Ganesan Kannan             Tirunelveli       2,67,540    1,87,358  70.00%     1,884       1.00%\n193      194         7              Subramaniyam M        Tiruppur (North)       3,26,277    2,16,314  66.30%     1,750       0.80%\n194      195         8            Senthil Kumar P.                 Coonoor       1,85,574    1,32,587  71.40%       469       0.40%\n195      196         8                   Rajendran            Erode (East)       2,14,592    1,44,922  67.50%     2,111       1.50%\n196      197         8        Thirumalaikumarasamy            Kadayanallur       2,63,128    1,86,768  71.00%     1,350       0.70%\n197      198         8               Chinnasami R.           Kinathukadavu       2,93,432    2,04,105  69.60%     1,265       0.60%\n198      199         8            Balasubramani .S              Kulithalai       2,07,792    1,82,170  87.70%       870       0.50%\n199      200         8                 Malaisamy R             Manamadurai       2,53,688    1,83,329  72.30%       647       0.40%\n200      201         8             Abdul Salam A.K                   Melur       2,34,129    1,71,744  73.40%       746       0.40%\n201      202         8                 R. Irulandi           Mudhukulathur       2,97,492    2,02,217  68.00%     1,133       0.60%\n202      203         8                    George M               Nagercoil       2,63,106    1,71,522  65.20%       527       0.30%\n203      204         8             Thiruppathi . S               Nanguneri       2,38,937    1,71,071  71.60%       660       0.40%\n204      205         8                     Shaju V         Padmanabhapuram       2,33,736    1,60,201  68.50%       410       0.30%\n205      206         8              Thiyagarajan P              Peravurani       2,04,407    1,60,603  78.60%       421       0.30%\n206      207         8              Kannappan V.S.                Pollachi       2,16,097    1,66,362  77.00%       747       0.50%\n207      208         8                  Vellaisamy             Pudukkottai       2,26,029    1,68,645  74.60%       667       0.40%\n208      209         8               S. Gurunathan              Radhapuram       2,37,643    1,69,516  71.30%       501       0.30%\n209      210         8               Sureshkumar S           Sankarankovil       2,32,201    1,75,244  75.50%       645       0.40%\n210      211         8                  Lingaraj G            Srivaikuntam       2,04,815    1,53,909  75.10%       806       0.50%\n211      212         8               Vellaisamy. V          Srivilliputhur       2,30,368    1,76,464  76.60%     1,119       0.60%\n212      213         8       Vidiyal Jaganathan V.            Thondamuthur       2,91,769    1,95,852  67.10%     1,315       0.70%\n213      214         8       Sayed Masnsoor Husain        Tiruppur (South)       2,46,541    1,61,721  65.60%     1,093       0.70%\n214      215         8                   Murugan.T             Usilampatti       2,69,103    1,99,454  74.10%       619       0.30%\n215      216         8                Sigaravel U.                Valparai       1,95,780    1,41,537  72.30%       580       0.40%\n216      217         8              Kasipandiyan K          Vasudevanallur       2,19,497    1,61,244  73.50%     1,198       0.70%\n217      218         8                 Muniasamy S            Vilathikulam       2,04,302    1,51,214  74.00%       560       0.40%\n218      219         8                 Kanagaraj G             Viralimalai       1,99,103    1,69,474  85.10%       415       0.20%\n219      220         9              A.Ramakrishnan           Bodinayakanur       2,57,098    1,99,613  77.60%       405       0.20%\n220      221         9                   Kanniah.T           Thirumangalam       2,61,153    2,02,432  77.50%       843       0.40%\n221      222         9                Alagappan Pl             Tiruppattur       2,65,915    1,96,751  74.00%       706       0.40%\n222      223         9               Palanichamy C              Vedasandur       2,46,896    1,96,302  79.50%       480       0.20%\n223      224        10                 Pandiyan M.        Krishnarayapuram       2,02,913    1,63,817  80.70%     1,327       0.80%\n224      225        11                    Selvam K              Aranthangi       2,11,467    1,53,822  72.70%       626       0.40%\n225      226        11                 Nagarajan B                  Palani       2,57,546    1,96,014  76.10%       490       0.30%\n226      227        11                 Hariharan R             Vilavancode       2,40,547    1,60,990  66.90%       398       0.30%\n227      228        12                 Shanmugam K            Oddanchatram       2,23,628    1,88,140  84.10%       367       0.20%\n228      229        13                Muniasamy A.               Tiruchuli       2,05,318    1,66,414  81.10%       260       0.20%\n229      230        13                    Pandi. V             Tiruvadanai       2,71,962    1,85,710  68.30%       522       0.30%'
>>> print(data.to_string())
       #      Position                   Candidate                 AC Name Total Electors Total Votes Turnout PMK Votes PMK Votes %
0          1         2                Annadurai. N                Edappadi       2,61,712    2,23,731  85.50%    56,681      25.30%
1          2         2         Guru @ Gurunathan.J             Jayankondam       2,50,259    2,02,088  80.80%    52,738      26.10%
2          3         2           Sathiyamoorthy. A        Pappireddippatti       2,43,140    2,07,287  85.30%    61,521      29.70%
3          4         2           Anbumani Ramadoss              Pennagaram       2,26,254    1,97,554  87.30%    58,402      29.60%
4          5         3                   Sekar K N                Ambattur       3,53,518    2,24,029  63.40%    16,635       7.40%
5          6         3              Elavazagan K L               Anaikattu       2,28,249    1,80,385  79.00%    24,711      13.70%
6          7         3                       Gopal                Anthiyur       2,05,788    1,68,035  81.70%    11,570       6.90%
7          8         3                    Arpudham               Arakkonam       2,17,390    1,63,392  75.20%    20,130      12.30%
8          9         3                 Rajasekar S                   Arani       2,55,752    2,07,796  81.20%    12,877       6.20%
9         10         3                 G.Karikalan                   Arcot       2,44,127    2,01,388  82.50%    35,043      17.40%
10        11         3                  Amsaveni G                   Attur       2,32,681    1,84,046  79.10%    18,363      10.00%
11        12         3                     A.Kumar                  Bargur       2,26,603    1,86,674  82.40%    18,407       9.90%
12        13         3              Ramanathan K V                 Bhavani       2,25,945    1,86,234  82.40%    20,727      11.10%
13        14         3                  Ashokkumar             Bhuvanagiri       2,38,798    1,89,722  79.40%    33,681      17.80%
14        15         3                  Arumugam.K            Chengalpattu       3,66,345    2,46,190  67.20%    20,899       8.50%
15        16         3                  Murugan. C                 Chengam       2,48,143    2,09,000  84.20%    15,114       7.20%
16        17         3                Srinivasan G                 Cheyyar       2,43,709    2,03,565  83.50%    37,491      18.40%
17        18         3                      Arul R             Chidambaram       2,28,166    1,68,905  74.00%    24,226      14.30%
18        19         3             Senthil. R. Dr.              Dharmapuri       2,50,333    2,05,225  82.00%    56,727      27.60%
19        20         3         Shanmugavel Murty.A              Gangavalli       2,17,595    1,74,215  80.10%    10,715       6.20%
20        21         3              Ganesh Kumar A                  Gingee       2,50,191    1,98,698  79.40%    28,515      14.40%
21        22         3                    Deepa .B              Gudiyattam       2,60,612    1,92,747  74.00%     7,505       3.90%
22        23         3                  Selvaraj M           Gummidipoondi       2,59,194    2,12,864  82.10%    43,055      20.20%
23        24         3                 Ponnusamy.G                Jolarpet       2,22,146    1,79,601  80.80%    17,516       9.80%
24        25         3                  Kalidass R            Kalasapakkam       2,18,565    1,84,349  84.30%    23,825      12.90%
25        26         3             P. Magesh Kumar            Kancheepuram       2,96,751    2,20,467  74.30%    30,102      13.70%
26        27         3               Shanmugam N T                 Katpadi       2,27,250    1,75,378  77.20%    12,728       7.30%
27        28         3             Edirolimanian G            Kilpennathur       2,34,104    1,96,123  83.80%    20,737      10.60%
28        29         3              Kusalakumari.C      Kilvaithinankuppam       2,04,298    1,63,236  79.90%    13,046       8.00%
29        30         3                     Kumar.S             Krishnagiri       2,44,487    1,98,237  81.10%    15,736       7.90%
30        31         3              Vaithilingam G                  Kunnam       2,54,896    2,02,020  79.30%    37,271      18.50%
31        32         3             Muthukrishnan S             Kurinjipadi       2,21,868    1,86,664  84.10%    22,705      12.20%
32        33         3                  Eraviraj G               Madavaram       3,97,265    2,64,427  66.60%    14,245       5.40%
33        34         3               A.Adhikesavan            Madurantakam       2,19,928    1,76,354  80.20%    16,215       9.20%
34        35         3             Rajashekaran Vr                  Mailam       2,10,950    1,69,489  80.30%    25,711      15.20%
35        36         3                  Ayyappan.A          Mayiladuthurai       2,34,079    1,67,168  71.40%    13,115       7.90%
36        37         3                    Mani.G.K                  Mettur       2,62,849    2,05,745  78.30%    49,939      24.30%
37        38         3                Tamilarasu.A                  Omalur       2,66,164    2,25,556  84.70%    48,721      21.60%
38        39         3                  Mannan. K.                Palacode       2,11,355    1,86,887  88.40%    31,612      16.90%
39        40         3              Dharmalingam.A                 Panruti       2,26,590    1,83,477  81.00%    18,666      10.20%
40        41         3                   Pandian A                 Ponneri       2,47,430    1,95,364  79.00%     9,586       4.90%
41        42         3                 Anbalagan.R               Poompuhar       2,56,713    1,91,280  74.50%    16,241       8.50%
42        43         3             Parthasarathy C             Poonamallee       3,09,083    2,36,722  76.60%    15,827       6.70%
43        44         3                Murali. M. K                 Ranipet       2,46,310    1,88,621  76.60%    23,850      12.60%
44        45         3              Pushpagandhi J               Rasipuram       2,22,650    1,84,074  82.70%     6,952       3.80%
45        46         3         Kathir Raasaratinam           Salem (North)       2,67,624    1,87,811  70.20%     7,975       4.30%
46        47         3                     Kumar K           Salem (South)       2,63,957    1,93,768  73.40%     6,325       3.30%
47        48         3                      Arul.R            Salem (West)       2,70,641    1,99,371  73.70%    29,982      15.00%
48        49         3                 Sivaraman S            Sankarapuram       2,51,971    2,02,263  80.30%    13,612       6.70%
49        50         3                    Kannan.P                 Sankari       2,56,471    2,12,929  83.00%    37,927      17.80%
50        51         3                 K.Saravanan               Sholingur       2,54,525    2,09,373  82.30%    50,827      24.30%
51        52         3                  Ramkumar.K         Shozhinganallur       5,75,773    3,38,365  58.80%    15,595       4.60%
52        53         3              Muthukumar.Pon                Sirkazhi       2,31,842    1,76,325  76.10%    14,890       8.40%
53        54         3                Muthuraman.C           Sriperumbudur       3,00,120    2,33,186  77.70%    18,185       7.80%
54        55         3                     Vasu. K              Thiruporur       2,50,050    1,99,025  79.60%    28,125      14.10%
55        56         3                  Balayogi V             Thiruvallur       2,54,359    2,04,826  80.50%    31,935      15.60%
56        57         3              Madahaiyan.R.S       Thiruvidaimarudur       2,33,519    1,83,030  78.40%    13,709       7.50%
57        58         3                  Kalidoss A              Tindivanam       2,20,510    1,73,038  78.50%    29,848      17.30%
58        59         3                  Balasakthi            Tirukkoyilur       2,38,318    1,86,328  78.20%    18,822      10.10%
59        60         3                    Raja.T.K              Tirupattur       2,26,179    1,76,650  78.10%    12,227       6.90%
60        61         3              Vaithilingam A               Tiruttani       2,73,887    2,20,333  80.40%    29,596      13.40%
61        62         3                   Pandian L          Tiruvannamalai       2,55,353    2,02,022  79.10%     7,916       3.90%
62        63         3                 T.N.Anguthi              Uthangarai       2,17,792    1,78,899  82.10%    23,500      13.10%
63        64         3             Gangadharan.Pon             Uthiramerur       2,42,572    1,97,126  81.30%    24,221      12.30%
64        65         3              Vadivelravanan               Vandavasi       2,23,241    1,79,055  80.20%    24,277      13.60%
65        66         3                    Sankar P                   Vanur       2,20,293    1,72,998  78.50%    27,240      15.80%
66        67         3                Samraj.A.R.B              Veerapandi       2,38,532    2,03,890  85.50%    17,218       8.40%
67        68         3               Tamil Selvi M            Veppanahalli       2,26,937    1,91,843  84.50%     5,476       2.90%
68        69         3                 Anbumani. C              Vikravandi       2,17,174    1,77,252  81.60%    41,428      23.40%
69        70         3                 Palanivel P              Villupuram       2,45,110    1,87,263  76.40%    36,456      19.50%
70        71         3            Tamizharasi P Dr            Vridhachalam       2,32,531    1,82,870  78.60%    29,340      16.00%
71        72         3                    Selvam.R                 Yercaud       2,58,758    2,19,430  84.80%    17,998       8.20%
72        73         4                 Arulmani .S                Alangudi       1,96,502    1,57,028  79.90%     5,514       3.50%
73        74         4           Thirumavalavan. K                Ariyalur       2,47,475    2,09,182  84.50%    13,529       6.50%
74        75         4            Anandakrishnan N                   Avadi       3,87,261    2,65,738  68.60%    12,428       4.70%
75        76         4                 Sadaiyappan                 Cheyyur       2,11,135    1,67,307  79.20%    17,892      10.70%
76        77         4        Thamaraikannan Pazha               Cuddalore       2,28,538    1,70,626  74.70%    16,905       9.90%
77        78         4                     Agnes F  Dr.Radhakrishnan Nagar       2,55,198    1,71,142  67.10%     3,011       1.80%
78        79         4                    S.Murali                   Harur       2,25,231    1,88,042  83.50%    27,747      14.80%
79        80         4                   Muniraj P                   Hosur       2,96,779    2,11,786  71.40%    10,309       4.90%
80        81         4            Senthamilselvi R            Kallakurichi       2,64,413    2,10,711  79.70%     9,736       4.60%
81        82         4                 Sozhan.Anbu     Kattumannarkoil(SC)       2,10,687    1,64,161  77.90%    25,890      15.80%
82        83         4                   Vanitha.A                Kilvelur       1,63,189    1,36,880  83.90%     2,637       1.90%
83        84         4               K.Venkatraman              Kumbakonam       2,46,071    1,86,234  75.70%     8,048       4.30%
84        85         4              Srinivasan N V             Maduravoyal       3,91,693    2,41,942  61.80%    17,328       7.20%
85        86         4         Balasubramaniyan. S              Mannargudi       2,40,899    1,85,336  76.90%     1,983       1.10%
86        87         4              Suresh Kumar N                Mylapore       2,57,032    1,52,344  59.30%     5,806       3.80%
87        88         4               Elavarasan. E                Nannilam       2,53,096    2,01,972  79.80%     5,060       2.50%
88        89         4                     Jagan K                 Neyveli       2,00,260    1,57,531  78.70%    19,749      12.50%
89        90         4                Alayamani .G               Papanasam       2,38,119    1,80,637  75.90%     4,963       2.80%
90        91         4             M.Sathiyaseelan              Perambalur       2,75,932    2,20,233  79.80%     4,222       1.90%
91        92         4                Velayutham.A                   Polur       2,25,566    1,94,484  86.20%    17,184       8.80%
92        93         4                 Pandiyan.Kp           Rishivandiyam       2,47,152    1,95,830  79.20%     8,148       4.20%
93        94         4              Sahadevan.T.R.                Saidapet       2,79,207    1,64,477  58.90%     5,913       3.60%
94        95         4                Arunrajan D.                  Thalli       2,28,512    1,86,900  81.80%     5,253       2.80%
95        96         4               Vanithamani D       Thiru-Vi-Ka-Nagar       2,15,120    1,33,765  62.20%     2,056       1.50%
96        97         4                Sivakumar .R              Thiruvarur       2,52,466    1,94,618  77.10%     1,787       0.90%
97        98         4            Vasanthakumari.R           Thiruvottiyur       2,86,872    1,87,144  65.20%     4,025       2.20%
98        99         4                  Archunan E          Tittagudi (SC)       2,06,909    1,58,219  76.50%    11,438       7.20%
99       100         4                     Balu K.           Ulundurpettai       2,72,569    2,26,647  83.20%    20,233       8.90%
100      101         4           Lakshmi Narayanan                 Vellore       2,47,628    1,68,879  68.20%     5,185       3.10%
101      102         5               Srinivasan R.                 Alandur       3,41,623    2,12,270  62.10%     7,194       3.40%
102      103         5                Akhilesh A M              Anna Nagar       2,85,165    1,68,933  59.20%     5,619       3.30%
103      104         5                 Vadivel.N.R            Bhavanisagar       2,37,600    1,93,571  81.50%     1,485       0.80%
104      105         5               A.V.A.Kassali  Chepauk-Thiruvallikeni       2,25,920    1,40,171  62.00%     2,511       1.80%
105      106         5               Parasuraman R                Dindigul       2,47,238    1,82,636  73.90%     2,718       1.50%
106      107         5                 Rajendran A                  Egmore       1,90,949    1,17,795  61.70%     1,814       1.50%
107      108         5                     S.Gopal                Kolathur       2,61,913    1,64,754  62.90%     3,022       1.80%
108      109         5            G. Ramachandiran              Kovilpatti       2,44,448    1,63,257  66.80%     1,075       0.70%
109      110         5              Ravichandran A            Madathukulam       2,24,447    1,69,397  75.50%     2,443       1.40%
110      111         5              Aasai Kumar R.           Madurai North       2,33,677    1,50,889  64.60%     2,039       1.40%
111      112         5                   Ragavan S                  Musiri       2,11,512    1,68,424  79.60%     1,423       0.80%
112      113         5                 Duraisamy E                Namakkal       2,43,892    1,90,613  78.20%     2,751       1.40%
113      114         5                 Ramoorthy N             Nilakkottai       2,16,344    1,72,722  79.80%     2,201       1.30%
114      115         5         Saravana Iyappan. M              Orathanadu       2,26,104    1,78,141  78.80%     1,444       0.80%
115      116         5                Venkatesan R              Pallavaram       4,03,787    2,45,381  60.80%     9,339       3.80%
116      117         5         M.Venkatesh Perumal                Perambur       2,88,901    1,85,514  64.20%     3,685       2.00%
117      118         5                    Susila K          Senthamangalam       2,32,916    1,87,253  80.40%     2,447       1.30%
118      119         5                    R Suresh                Tambaram       3,72,883    2,30,348  61.80%     7,631       3.30%
119      120         5                Rajamohan. S       Thiruthuraipoondi       2,22,380    1,73,852  78.20%     2,005       1.20%
120      121         5                 R.Kanakaraj            Thiruvaiyaru       2,48,188    2,01,043  81.00%     1,571       0.80%
121      122         5                    Vinoth.V        Thiyagarayanagar       2,40,352    1,38,412  57.60%     5,071       3.70%
122      123         5                    Rangan V         Thousand Lights       2,43,386    1,38,770  57.00%     3,968       2.90%
123      124         5            Vijayaraghavan.K  Tiruchirappalli (West)       2,53,551    1,75,323  69.10%     1,780       1.00%
124      125         5                   Balraj M.          Udhagamandalam       2,00,138    1,37,243  68.60%       781       0.60%
125      126         5              Kirubakaran.R.             Vaniyambadi       2,23,883    1,70,864  76.30%     9,283       5.40%
126      127         5                 Usha Kannan              Vedaranyam       1,81,787    1,45,597  80.10%     2,081       1.40%
127      128         5            Vinoba Bhoopathy               Velachery       2,96,329    1,71,297  57.80%     6,809       4.00%
128      129         5               V.Subramanian             Villivakkam       2,52,292    1,46,675  58.10%     4,193       2.90%
129      130         5                C.H. Jayarao           Virugampakkam       2,86,046    1,67,442  58.50%     3,945       2.40%
130      131         6                R. Anbalagan            Ambasamudram       2,33,876    1,69,487  72.50%     1,310       0.80%
131      132         6                 Ameen Basha                   Ambur       2,10,433    1,59,443  75.80%     4,643       2.90%
132      133         6              Aravindkumar.D           Aruppukkottai       2,04,976    1,62,400  79.20%       817       0.50%
133      134         6     Nirmala Gnanasoundari I                  Athoor       2,69,948    2,27,147  84.10%       671       0.30%
134      135         6             Kamaraj Natesan      Coimbatore (North)       3,02,353    1,84,308  61.00%     2,196       1.20%
135      136         6                 Madhavan. K         Dharapuram (SC)       2,36,823    1,80,028  76.00%     1,515       0.80%
136      137         6                    Arumugam            Erode (West)       2,55,003    1,85,964  72.90%     3,000       1.60%
137      138         6     Murugesan @ Murugesh R.                 Gudalur       1,78,142    1,29,270  72.60%       684       0.50%
138      139         6               Sureshkumar R                 Harbour       1,82,820    1,02,137  55.90%     1,011       1.00%
139      140         6               Amirtavalli V                Kangayam       2,31,742    1,81,287  78.20%     1,544       0.90%
140      141         6       Hilman Bruce Edwin. S           Kanniyakumari       2,81,262    2,08,354  74.10%       712       0.30%
141      142         6               Thangavelu A.         Kavundampalayam       4,06,349    2,67,126  65.70%     2,533       1.00%
142      143         6                 Alexander J               Killiyoor       2,49,258    1,52,131  61.00%       615       0.40%
143      144         6                    Murthy S           Kumarapalayam       2,32,414    1,83,658  79.00%     2,773       1.50%
144      145         6                   Alaguraja            Madurai East       2,86,211    2,11,227  73.80%     1,113       0.50%
145      146         6              Krishnakumar R            Madurai West       2,79,424    1,81,421  64.90%       927       0.50%
146      147         6                   Prince. M           Manachanallur       2,17,178    1,77,694  81.80%     1,212       0.70%
147      148         6                  Moorthi. K           Mettuppalayam       2,73,728    2,07,353  75.80%     1,870       0.90%
148      149         6                  Nachimuthu            Modakkurichi       2,21,957    1,73,953  78.40%     2,809       1.60%
149      150         6                    Balraj.A            Nagapattinam       1,84,181    1,33,443  72.50%     1,036       0.80%
150      151         6                 Seerangan K                  Natham       2,58,472    2,05,167  79.40%     1,155       0.60%
151      152         6             Murugaperumal.R             Ottapidaram       2,17,224    1,57,784  72.60%     1,066       0.70%
152      153         6                 Thangaraj.R              Paramakudi       2,46,166    1,67,411  68.00%       690       0.40%
153      154         6                  Ramesh Pon         Paramathi-Velur       2,10,835    1,73,648  82.40%     3,740       2.20%
154      155         6                  Lakshmi. C            Pattukkottai       2,26,518    1,64,349  72.60%     3,607       2.20%
155      156         6                    Kannan.R             Periyakulam       2,58,145    1,90,735  73.90%     1,025       0.50%
156      157         6                 Kumaresan.P              Perundurai       2,10,871    1,80,272  85.50%     1,498       0.80%
157      158         6              Lakshmanan. P.             Rajapalayam       2,21,788    1,68,398  75.90%     1,073       0.60%
158      159         6                  Muthaiah S             Sholavandan       2,06,777    1,64,394  79.50%       857       0.50%
159      160         6           Ashok Jayendar P.             Singanallur       3,04,591    1,84,799  60.70%     2,865       1.60%
160      161         6              Thilagabama M.                Sivakasi       2,34,432    1,72,998  73.80%     1,350       0.80%
161      162         6             Umamaheshwari.S               Srirangam       2,81,063    2,21,279  78.70%     1,548       0.70%
162      163         6                    Suresh A              Thirumayam       2,05,506    1,56,654  76.20%       950       0.60%
163      164         6               Balamurugan K       Thiruparankundram       2,79,299    1,94,369  69.60%     1,237       0.60%
164      165         6                Dilipkumar.K           Thiruverumbur       2,67,527    1,80,292  67.40%     1,498       0.80%
165      166         6              Chinnadurai.M.            Thoothukkudi       2,75,218    1,86,311  67.70%     1,069       0.60%
166      167         6  Kumara Gurupara Adithan D.             Tiruchendur       2,23,973    1,64,994  73.70%       578       0.40%
167      168         6                 Sridhar .B.  Tiruchirappalli (East)       2,40,767    1,62,656  67.60%     1,866       1.20%
168      169         6                 Duraisamy P          Udumalaipettai       2,50,547    1,79,611  71.70%     1,975       1.10%
169      170         6             Ganeshperumal.P            Virudhunagar       2,05,887    1,50,512  73.10%       556       0.40%
170      171         7               P.Gunasekaran               Alangulam       2,43,056    1,91,237  78.70%       674       0.40%
171      172         7                      Ravi.K               Andipatti       2,52,747    1,96,700  77.80%       817       0.40%
172      173         7               Marimuthu K K           Avanashi (SC)       2,48,719    1,90,528  76.60%     1,480       0.80%
173      174         7             Palanychamy Ki.      Coimbatore (South)       2,42,869    1,50,202  61.80%     1,111       0.70%
174      175         7         Alexanderrajkumar A                Colachel       2,60,607    1,65,612  63.50%       772       0.50%
175      176         7           Pon. Katchikannan                  Cumbum       2,62,147    1,91,863  73.20%       763       0.40%
176      177         7            Palanimanickam.M         Gandharvakottai       1,84,576    1,44,534  78.30%       530       0.40%
177      178         7                   Kuppusamy       Gobichettipalayam       2,41,198    2,01,877  83.70%     1,045       0.50%
178      179         7               Duraipandi Pr               Karaikudi       2,82,460    1,98,667  70.30%       897       0.50%
179      180         7                Murugesan .M                   Karur       2,31,209    1,83,218  79.20%     1,376       0.80%
180      181         7             Umamaheswaran R                 Lalgudi       2,01,236    1,64,601  81.80%       745       0.50%
181      182         7                    Selvam T         Madurai Central       2,34,511    1,49,299  63.70%     1,007       0.70%
182      183         7              Mari Selvam. S           Madurai South       2,20,259    1,43,693  65.20%       864       0.60%
183      184         7           Leema Sivakumar A              Manapparai       2,61,856    2,02,592  77.40%       826       0.40%
184      185         7             Nishthar Ali .S           Palayamkottai       2,54,284    1,51,701  59.70%     1,315       0.90%
185      186         7                    Kumar. S                Palladam       3,25,238    2,34,062  72.00%     2,292       1.00%
186      187         7                 Perumal T S               Royapuram       1,86,386    1,19,769  64.30%     2,126       1.80%
187      188         7             Balakrishnan M.                  Sattur       2,22,271    1,74,484  78.50%       768       0.40%
188      189         7               Rajasekaran.N               Sivaganga       2,71,108    1,87,812  69.30%     1,284       0.70%
189      190         7                Ganesan P.K.                   Sulur       2,79,722    2,09,433  74.90%     1,687       0.80%
190      191         7               Seetharaman P                 Tenkasi       2,61,504    1,99,384  76.20%     1,222       0.60%
191      192         7                      Raja S            Tiruchengodu       2,18,127    1,74,285  79.90%     2,012       1.20%
192      193         7              Ganesan Kannan             Tirunelveli       2,67,540    1,87,358  70.00%     1,884       1.00%
193      194         7              Subramaniyam M        Tiruppur (North)       3,26,277    2,16,314  66.30%     1,750       0.80%
194      195         8            Senthil Kumar P.                 Coonoor       1,85,574    1,32,587  71.40%       469       0.40%
195      196         8                   Rajendran            Erode (East)       2,14,592    1,44,922  67.50%     2,111       1.50%
196      197         8        Thirumalaikumarasamy            Kadayanallur       2,63,128    1,86,768  71.00%     1,350       0.70%
197      198         8               Chinnasami R.           Kinathukadavu       2,93,432    2,04,105  69.60%     1,265       0.60%
198      199         8            Balasubramani .S              Kulithalai       2,07,792    1,82,170  87.70%       870       0.50%
199      200         8                 Malaisamy R             Manamadurai       2,53,688    1,83,329  72.30%       647       0.40%
200      201         8             Abdul Salam A.K                   Melur       2,34,129    1,71,744  73.40%       746       0.40%
201      202         8                 R. Irulandi           Mudhukulathur       2,97,492    2,02,217  68.00%     1,133       0.60%
202      203         8                    George M               Nagercoil       2,63,106    1,71,522  65.20%       527       0.30%
203      204         8             Thiruppathi . S               Nanguneri       2,38,937    1,71,071  71.60%       660       0.40%
204      205         8                     Shaju V         Padmanabhapuram       2,33,736    1,60,201  68.50%       410       0.30%
205      206         8              Thiyagarajan P              Peravurani       2,04,407    1,60,603  78.60%       421       0.30%
206      207         8              Kannappan V.S.                Pollachi       2,16,097    1,66,362  77.00%       747       0.50%
207      208         8                  Vellaisamy             Pudukkottai       2,26,029    1,68,645  74.60%       667       0.40%
208      209         8               S. Gurunathan              Radhapuram       2,37,643    1,69,516  71.30%       501       0.30%
209      210         8               Sureshkumar S           Sankarankovil       2,32,201    1,75,244  75.50%       645       0.40%
210      211         8                  Lingaraj G            Srivaikuntam       2,04,815    1,53,909  75.10%       806       0.50%
211      212         8               Vellaisamy. V          Srivilliputhur       2,30,368    1,76,464  76.60%     1,119       0.60%
212      213         8       Vidiyal Jaganathan V.            Thondamuthur       2,91,769    1,95,852  67.10%     1,315       0.70%
213      214         8       Sayed Masnsoor Husain        Tiruppur (South)       2,46,541    1,61,721  65.60%     1,093       0.70%
214      215         8                   Murugan.T             Usilampatti       2,69,103    1,99,454  74.10%       619       0.30%
215      216         8                Sigaravel U.                Valparai       1,95,780    1,41,537  72.30%       580       0.40%
216      217         8              Kasipandiyan K          Vasudevanallur       2,19,497    1,61,244  73.50%     1,198       0.70%
217      218         8                 Muniasamy S            Vilathikulam       2,04,302    1,51,214  74.00%       560       0.40%
218      219         8                 Kanagaraj G             Viralimalai       1,99,103    1,69,474  85.10%       415       0.20%
219      220         9              A.Ramakrishnan           Bodinayakanur       2,57,098    1,99,613  77.60%       405       0.20%
220      221         9                   Kanniah.T           Thirumangalam       2,61,153    2,02,432  77.50%       843       0.40%
221      222         9                Alagappan Pl             Tiruppattur       2,65,915    1,96,751  74.00%       706       0.40%
222      223         9               Palanichamy C              Vedasandur       2,46,896    1,96,302  79.50%       480       0.20%
223      224        10                 Pandiyan M.        Krishnarayapuram       2,02,913    1,63,817  80.70%     1,327       0.80%
224      225        11                    Selvam K              Aranthangi       2,11,467    1,53,822  72.70%       626       0.40%
225      226        11                 Nagarajan B                  Palani       2,57,546    1,96,014  76.10%       490       0.30%
226      227        11                 Hariharan R             Vilavancode       2,40,547    1,60,990  66.90%       398       0.30%
227      228        12                 Shanmugam K            Oddanchatram       2,23,628    1,88,140  84.10%       367       0.20%
228      229        13                Muniasamy A.               Tiruchuli       2,05,318    1,66,414  81.10%       260       0.20%
229      230        13                    Pandi. V             Tiruvadanai       2,71,962    1,85,710  68.30%       522       0.30%
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 230 entries, 0 to 229
Data columns (total 9 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0     #             230 non-null    int64 
 1   Position        230 non-null    int64 
 2   Candidate       230 non-null    object
 3   AC Name         230 non-null    object
 4   Total Electors  230 non-null    object
 5   Total Votes     230 non-null    object
 6   Turnout         230 non-null    object
 7   PMK Votes       230 non-null    object
 8   PMK Votes %     230 non-null    object
dtypes: int64(2), object(7)
memory usage: 16.3+ KB
>>> #what was the total number of PMK votes
>>> data['PMK Votes']
0      56,681
1      52,738
2      61,521
3      58,402
4      16,635
        ...  
225       490
226       398
227       367
228       260
229       522
Name: PMK Votes, Length: 230, dtype: object
>>> data['PMK Votes'].unique()
array(['56,681', '52,738', '61,521', '58,402', '16,635', '24,711',
       '11,570', '20,130', '12,877', '35,043', '18,363', '18,407',
       '20,727', '33,681', '20,899', '15,114', '37,491', '24,226',
       '56,727', '10,715', '28,515', '7,505', '43,055', '17,516',
       '23,825', '30,102', '12,728', '20,737', '13,046', '15,736',
       '37,271', '22,705', '14,245', '16,215', '25,711', '13,115',
       '49,939', '48,721', '31,612', '18,666', '9,586', '16,241',
       '15,827', '23,850', '6,952', '7,975', '6,325', '29,982', '13,612',
       '37,927', '50,827', '15,595', '14,890', '18,185', '28,125',
       '31,935', '13,709', '29,848', '18,822', '12,227', '29,596',
       '7,916', '23,500', '24,221', '24,277', '27,240', '17,218', '5,476',
       '41,428', '36,456', '29,340', '17,998', '5,514', '13,529',
       '12,428', '17,892', '16,905', '3,011', '27,747', '10,309', '9,736',
       '25,890', '2,637', '8,048', '17,328', '1,983', '5,806', '5,060',
       '19,749', '4,963', '4,222', '17,184', '8,148', '5,913', '5,253',
       '2,056', '1,787', '4,025', '11,438', '20,233', '5,185', '7,194',
       '5,619', '1,485', '2,511', '2,718', '1,814', '3,022', '1,075',
       '2,443', '2,039', '1,423', '2,751', '2,201', '1,444', '9,339',
       '3,685', '2,447', '7,631', '2,005', '1,571', '5,071', '3,968',
       '1,780', '781', '9,283', '2,081', '6,809', '4,193', '3,945',
       '1,310', '4,643', '817', '671', '2,196', '1,515', '3,000', '684',
       '1,011', '1,544', '712', '2,533', '615', '2,773', '1,113', '927',
       '1,212', '1,870', '2,809', '1,036', '1,155', '1,066', '690',
       '3,740', '3,607', '1,025', '1,498', '1,073', '857', '2,865',
       '1,350', '1,548', '950', '1,237', '1,069', '578', '1,866', '1,975',
       '556', '674', '1,480', '1,111', '772', '763', '530', '1,045',
       '897', '1,376', '745', '1,007', '864', '826', '1,315', '2,292',
       '2,126', '768', '1,284', '1,687', '1,222', '2,012', '1,884',
       '1,750', '469', '2,111', '1,265', '870', '647', '746', '1,133',
       '527', '660', '410', '421', '747', '667', '501', '645', '806',
       '1,119', '1,093', '619', '580', '1,198', '560', '415', '405',
       '843', '706', '480', '1,327', '626', '490', '398', '367', '260',
       '522'], dtype=object)
>>> data['PMK Votes'].sum()
'56,68152,73861,52158,40216,63524,71111,57020,13012,87735,04318,36318,40720,72733,68120,89915,11437,49124,22656,72710,71528,5157,50543,05517,51623,82530,10212,72820,73713,04615,73637,27122,70514,24516,21525,71113,11549,93948,72131,61218,6669,58616,24115,82723,8506,9527,9756,32529,98213,61237,92750,82715,59514,89018,18528,12531,93513,70929,84818,82212,22729,5967,91623,50024,22124,27727,24017,2185,47641,42836,45629,34017,9985,51413,52912,42817,89216,9053,01127,74710,3099,73625,8902,6378,04817,3281,9835,8065,06019,7494,9634,22217,1848,1485,9135,2532,0561,7874,02511,43820,2335,1857,1945,6191,4852,5112,7181,8143,0221,0752,4432,0391,4232,7512,2011,4449,3393,6852,4477,6312,0051,5715,0713,9681,7807819,2832,0816,8094,1933,9451,3104,6438176712,1961,5153,0006841,0111,5447122,5336152,7731,1139271,2121,8702,8091,0361,1551,0666903,7403,6071,0251,4981,0738572,8651,3501,5489501,2371,4981,0695781,8661,9755566748171,4801,1117727635301,0458971,3767451,0078648261,3152,2922,1267681,2841,6871,2222,0121,8841,7504692,1111,3501,2658706477461,1335276604104217476675016458061,1191,3151,0936195801,1985604154058437064801,327626490398367260522'
>>> data['PMK Votes'].tail()
225    490
226    398
227    367
228    260
229    522
Name: PMK Votes, dtype: object
>>> #PMK max vote
>>> data['PMK Votes'].max()
'950'
>>> data
       #      Position            Candidate  ... Turnout PMK Votes PMK Votes %
0          1         2         Annadurai. N  ...  85.50%    56,681      25.30%
1          2         2  Guru @ Gurunathan.J  ...  80.80%    52,738      26.10%
2          3         2    Sathiyamoorthy. A  ...  85.30%    61,521      29.70%
3          4         2    Anbumani Ramadoss  ...  87.30%    58,402      29.60%
4          5         3            Sekar K N  ...  63.40%    16,635       7.40%
..       ...       ...                  ...  ...     ...       ...         ...
225      226        11          Nagarajan B  ...  76.10%       490       0.30%
226      227        11          Hariharan R  ...  66.90%       398       0.30%
227      228        12          Shanmugam K  ...  84.10%       367       0.20%
228      229        13         Muniasamy A.  ...  81.10%       260       0.20%
229      230        13             Pandi. V  ...  68.30%       522       0.30%

[230 rows x 9 columns]
>>> #PMK min vote
>>> data['PMK Votes'].min()
'1,007'
>>> data['PMK Votes'].max()
'950'
>>> #how many 2rd position are there
>>> data['Position'].unique()
array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13], dtype=int64)
>>> data['Position'].unique(2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    data['Position'].unique(2)
TypeError: unique() takes 1 positional argument but 2 were given
>>> data['Position'].unique()=[2]
SyntaxError: cannot assign to function call
>>> data['Position'].count(2)

Warning (from warnings module):
  File "<pyshell#24>", line 1
FutureWarning: Using the level keyword in DataFrame and Series aggregations is deprecated and will be removed in a future version. Use groupby instead. ser.count(level=1) should use ser.groupby(level=1).count().
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    data['Position'].count(2)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 1937, in count
    raise ValueError("Series.count level is only valid with a MultiIndex")
ValueError: Series.count level is only valid with a MultiIndex
>>> data['Position'].count(level=2)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data['Position'].count(level=2)
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\series.py", line 1937, in count
    raise ValueError("Series.count level is only valid with a MultiIndex")
ValueError: Series.count level is only valid with a MultiIndex
>>> data['Position'].count(null)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    data['Position'].count(null)
NameError: name 'null' is not defined
>>> data.count(axis='columns')
0      9
1      9
2      9
3      9
4      9
      ..
225    9
226    9
227    9
228    9
229    9
Length: 230, dtype: int64
>>> data.count()
  #               230
Position          230
Candidate         230
AC Name           230
Total Electors    230
Total Votes       230
Turnout           230
PMK Votes         230
PMK Votes %       230
dtype: int64
>>> data.count(axis=1)
0      9
1      9
2      9
3      9
4      9
      ..
225    9
226    9
227    9
228    9
229    9
Length: 230, dtype: int64
>>> #total index value count
>>> index=pd.Index(data)
>>> index
Index([             (1, 2, 'Annadurai. N', 'Edappadi', '2,61,712', '2,23,731', '85.50%', '56,681', '25.30%'),
          (2, 2, 'Guru @ Gurunathan.J', 'Jayankondam', '2,50,259', '2,02,088', '80.80%', '52,738', '26.10%'),
       (3, 2, 'Sathiyamoorthy. A', 'Pappireddippatti', '2,43,140', '2,07,287', '85.30%', '61,521', '29.70%'),
             (4, 2, 'Anbumani Ramadoss', 'Pennagaram', '2,26,254', '1,97,554', '87.30%', '58,402', '29.60%'),
                        (5, 3, 'Sekar K N', 'Ambattur', '3,53,518', '2,24,029', '63.40%', '16,635', '7.40%'),
                 (6, 3, 'Elavazagan K L', 'Anaikattu', '2,28,249', '1,80,385', '79.00%', '24,711', '13.70%'),
                            (7, 3, 'Gopal', 'Anthiyur', '2,05,788', '1,68,035', '81.70%', '11,570', '6.90%'),
                       (8, 3, 'Arpudham', 'Arakkonam', '2,17,390', '1,63,392', '75.20%', '20,130', '12.30%'),
                         (9, 3, 'Rajasekar S', 'Arani', '2,55,752', '2,07,796', '81.20%', '12,877', '6.20%'),
                       (10, 3, 'G.Karikalan', 'Arcot', '2,44,127', '2,01,388', '82.50%', '35,043', '17.40%'),
       ...
                    (221, 9, 'Kanniah.T', 'Thirumangalam', '2,61,153', '2,02,432', '77.50%', '843', '0.40%'),
                   (222, 9, 'Alagappan Pl', 'Tiruppattur', '2,65,915', '1,96,751', '74.00%', '706', '0.40%'),
                   (223, 9, 'Palanichamy C', 'Vedasandur', '2,46,896', '1,96,302', '79.50%', '480', '0.20%'),
            (224, 10, 'Pandiyan M.', 'Krishnarayapuram', '2,02,913', '1,63,817', '80.70%', '1,327', '0.80%'),
                       (225, 11, 'Selvam K', 'Aranthangi', '2,11,467', '1,53,822', '72.70%', '626', '0.40%'),
                        (226, 11, 'Nagarajan B', 'Palani', '2,57,546', '1,96,014', '76.10%', '490', '0.30%'),
                   (227, 11, 'Hariharan R', 'Vilavancode', '2,40,547', '1,60,990', '66.90%', '398', '0.30%'),
                  (228, 12, 'Shanmugam K', 'Oddanchatram', '2,23,628', '1,88,140', '84.10%', '367', '0.20%'),
                    (229, 13, 'Muniasamy A.', 'Tiruchuli', '2,05,318', '1,66,414', '81.10%', '260', '0.20%'),
                      (230, 13, 'Pandi. V', 'Tiruvadanai', '2,71,962', '1,85,710', '68.30%', '522', '0.30%')],
      dtype='object', length=230)
>>> index=pd.Index(data,name='Position')
>>> index
Index([             (1, 2, 'Annadurai. N', 'Edappadi', '2,61,712', '2,23,731', '85.50%', '56,681', '25.30%'),
          (2, 2, 'Guru @ Gurunathan.J', 'Jayankondam', '2,50,259', '2,02,088', '80.80%', '52,738', '26.10%'),
       (3, 2, 'Sathiyamoorthy. A', 'Pappireddippatti', '2,43,140', '2,07,287', '85.30%', '61,521', '29.70%'),
             (4, 2, 'Anbumani Ramadoss', 'Pennagaram', '2,26,254', '1,97,554', '87.30%', '58,402', '29.60%'),
                        (5, 3, 'Sekar K N', 'Ambattur', '3,53,518', '2,24,029', '63.40%', '16,635', '7.40%'),
                 (6, 3, 'Elavazagan K L', 'Anaikattu', '2,28,249', '1,80,385', '79.00%', '24,711', '13.70%'),
                            (7, 3, 'Gopal', 'Anthiyur', '2,05,788', '1,68,035', '81.70%', '11,570', '6.90%'),
                       (8, 3, 'Arpudham', 'Arakkonam', '2,17,390', '1,63,392', '75.20%', '20,130', '12.30%'),
                         (9, 3, 'Rajasekar S', 'Arani', '2,55,752', '2,07,796', '81.20%', '12,877', '6.20%'),
                       (10, 3, 'G.Karikalan', 'Arcot', '2,44,127', '2,01,388', '82.50%', '35,043', '17.40%'),
       ...
                    (221, 9, 'Kanniah.T', 'Thirumangalam', '2,61,153', '2,02,432', '77.50%', '843', '0.40%'),
                   (222, 9, 'Alagappan Pl', 'Tiruppattur', '2,65,915', '1,96,751', '74.00%', '706', '0.40%'),
                   (223, 9, 'Palanichamy C', 'Vedasandur', '2,46,896', '1,96,302', '79.50%', '480', '0.20%'),
            (224, 10, 'Pandiyan M.', 'Krishnarayapuram', '2,02,913', '1,63,817', '80.70%', '1,327', '0.80%'),
                       (225, 11, 'Selvam K', 'Aranthangi', '2,11,467', '1,53,822', '72.70%', '626', '0.40%'),
                        (226, 11, 'Nagarajan B', 'Palani', '2,57,546', '1,96,014', '76.10%', '490', '0.30%'),
                   (227, 11, 'Hariharan R', 'Vilavancode', '2,40,547', '1,60,990', '66.90%', '398', '0.30%'),
                  (228, 12, 'Shanmugam K', 'Oddanchatram', '2,23,628', '1,88,140', '84.10%', '367', '0.20%'),
                    (229, 13, 'Muniasamy A.', 'Tiruchuli', '2,05,318', '1,66,414', '81.10%', '260', '0.20%'),
                      (230, 13, 'Pandi. V', 'Tiruvadanai', '2,71,962', '1,85,710', '68.30%', '522', '0.30%')],
      dtype='object', name='Position', length=230)
>>> index.value_counts()
(1, 2, Annadurai. N, Edappadi, 2,61,712, 2,23,731, 85.50%, 56,681, 25.30%)               1
(145, 6, Alaguraja, Madurai East, 2,86,211, 2,11,227, 73.80%, 1,113, 0.50%)              1
(147, 6, Prince. M, Manachanallur, 2,17,178, 1,77,694, 81.80%, 1,212, 0.70%)             1
(148, 6, Moorthi. K, Mettuppalayam, 2,73,728, 2,07,353, 75.80%, 1,870, 0.90%)            1
(149, 6, Nachimuthu, Modakkurichi, 2,21,957, 1,73,953, 78.40%, 2,809, 1.60%)             1
                                                                                        ..
(81, 4, Senthamilselvi R, Kallakurichi, 2,64,413, 2,10,711, 79.70%, 9,736, 4.60%)        1
(82, 4, Sozhan.Anbu, Kattumannarkoil(SC), 2,10,687, 1,64,161, 77.90%, 25,890, 15.80%)    1
(83, 4, Vanitha.A, Kilvelur, 1,63,189, 1,36,880, 83.90%, 2,637, 1.90%)                   1
(84, 4, K.Venkatraman, Kumbakonam, 2,46,071, 1,86,234, 75.70%, 8,048, 4.30%)             1
(230, 13, Pandi. V, Tiruvadanai, 2,71,962, 1,85,710, 68.30%, 522, 0.30%)                 1
Name: Position, Length: 230, dtype: int64
>>> data.dropna().shape
(230, 9)
>>> data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 230 entries, 0 to 229
Data columns (total 9 columns):
 #   Column          Non-Null Count  Dtype 
---  ------          --------------  ----- 
 0     #             230 non-null    int64 
 1   Position        230 non-null    int64 
 2   Candidate       230 non-null    object
 3   AC Name         230 non-null    object
 4   Total Electors  230 non-null    object
 5   Total Votes     230 non-null    object
 6   Turnout         230 non-null    object
 7   PMK Votes       230 non-null    object
 8   PMK Votes %     230 non-null    object
dtypes: int64(2), object(7)
memory usage: 16.3+ KB
>>> data['Candidate'].unique()
array(['Annadurai. N', 'Guru @ Gurunathan.J', 'Sathiyamoorthy. A',
       'Anbumani Ramadoss', 'Sekar K N', 'Elavazagan K L', 'Gopal',
       'Arpudham', 'Rajasekar S', 'G.Karikalan', 'Amsaveni G', 'A.Kumar',
       'Ramanathan K V', 'Ashokkumar', 'Arumugam.K', 'Murugan. C',
       'Srinivasan G', 'Arul R', 'Senthil. R. Dr.', 'Shanmugavel Murty.A',
       'Ganesh Kumar A', 'Deepa .B', 'Selvaraj M', 'Ponnusamy.G',
       'Kalidass R', 'P. Magesh Kumar', 'Shanmugam N T',
       'Edirolimanian G', 'Kusalakumari.C', 'Kumar.S', 'Vaithilingam G',
       'Muthukrishnan S', 'Eraviraj G', 'A.Adhikesavan',
       'Rajashekaran Vr', 'Ayyappan.A', 'Mani.G.K', 'Tamilarasu.A',
       'Mannan. K.', 'Dharmalingam.A', 'Pandian A', 'Anbalagan.R',
       'Parthasarathy C', 'Murali. M. K', 'Pushpagandhi J',
       'Kathir Raasaratinam', 'Kumar K', 'Arul.R', 'Sivaraman S',
       'Kannan.P', 'K.Saravanan', 'Ramkumar.K', 'Muthukumar.Pon',
       'Muthuraman.C', 'Vasu. K', 'Balayogi V', 'Madahaiyan.R.S',
       'Kalidoss A', 'Balasakthi', 'Raja.T.K', 'Vaithilingam A',
       'Pandian L', 'T.N.Anguthi', 'Gangadharan.Pon', 'Vadivelravanan',
       'Sankar P', 'Samraj.A.R.B', 'Tamil Selvi M', 'Anbumani. C',
       'Palanivel P', 'Tamizharasi P Dr', 'Selvam.R', 'Arulmani .S',
       'Thirumavalavan. K', 'Anandakrishnan N', 'Sadaiyappan',
       'Thamaraikannan Pazha', 'Agnes F', 'S.Murali', 'Muniraj P',
       'Senthamilselvi R', 'Sozhan.Anbu', 'Vanitha.A', 'K.Venkatraman',
       'Srinivasan N V', 'Balasubramaniyan. S', 'Suresh Kumar N',
       'Elavarasan. E', 'Jagan K', 'Alayamani .G', 'M.Sathiyaseelan',
       'Velayutham.A', 'Pandiyan.Kp', 'Sahadevan.T.R.', 'Arunrajan D.',
       'Vanithamani D', 'Sivakumar .R', 'Vasanthakumari.R', 'Archunan E',
       'Balu K.', 'Lakshmi Narayanan', 'Srinivasan R.', 'Akhilesh A M',
       'Vadivel.N.R', 'A.V.A.Kassali', 'Parasuraman R', 'Rajendran A',
       'S.Gopal', 'G. Ramachandiran', 'Ravichandran A', 'Aasai Kumar R.',
       'Ragavan S', 'Duraisamy E', 'Ramoorthy N', 'Saravana Iyappan. M',
       'Venkatesan R', 'M.Venkatesh Perumal', 'Susila K', 'R Suresh',
       'Rajamohan. S', 'R.Kanakaraj', 'Vinoth.V', 'Rangan V',
       'Vijayaraghavan.K', 'Balraj M.', 'Kirubakaran.R.', 'Usha Kannan',
       'Vinoba Bhoopathy', 'V.Subramanian', 'C.H. Jayarao',
       'R. Anbalagan', 'Ameen Basha', 'Aravindkumar.D',
       'Nirmala Gnanasoundari I', 'Kamaraj Natesan', 'Madhavan. K',
       'Arumugam', 'Murugesan @ Murugesh R.', 'Sureshkumar R',
       'Amirtavalli V', 'Hilman Bruce Edwin. S', 'Thangavelu A.',
       'Alexander J', 'Murthy S', 'Alaguraja', 'Krishnakumar R',
       'Prince. M', 'Moorthi. K', 'Nachimuthu', 'Balraj.A', 'Seerangan K',
       'Murugaperumal.R', 'Thangaraj.R', 'Ramesh Pon', 'Lakshmi. C',
       'Kannan.R', 'Kumaresan.P', 'Lakshmanan. P.', 'Muthaiah S',
       'Ashok Jayendar P.', 'Thilagabama M.', 'Umamaheshwari.S',
       'Suresh A', 'Balamurugan K', 'Dilipkumar.K', 'Chinnadurai.M.',
       'Kumara Gurupara Adithan D.', 'Sridhar .B.', 'Duraisamy P',
       'Ganeshperumal.P', 'P.Gunasekaran', 'Ravi.K', 'Marimuthu K K',
       'Palanychamy Ki.', 'Alexanderrajkumar A', 'Pon. Katchikannan',
       'Palanimanickam.M', 'Kuppusamy', 'Duraipandi Pr', 'Murugesan .M',
       'Umamaheswaran R', 'Selvam T', 'Mari Selvam. S',
       'Leema Sivakumar A', 'Nishthar Ali .S', 'Kumar. S', 'Perumal T S',
       'Balakrishnan M.', 'Rajasekaran.N', 'Ganesan P.K.',
       'Seetharaman P', 'Raja S', 'Ganesan Kannan', 'Subramaniyam M',
       'Senthil Kumar P.', 'Rajendran', 'Thirumalaikumarasamy',
       'Chinnasami R.', 'Balasubramani .S', 'Malaisamy R',
       'Abdul Salam A.K', 'R. Irulandi', 'George M', 'Thiruppathi . S',
       'Shaju V', 'Thiyagarajan P', 'Kannappan V.S.', 'Vellaisamy',
       'S. Gurunathan', 'Sureshkumar S', 'Lingaraj G', 'Vellaisamy. V',
       'Vidiyal Jaganathan V.', 'Sayed Masnsoor Husain', 'Murugan.T',
       'Sigaravel U.', 'Kasipandiyan K', 'Muniasamy S', 'Kanagaraj G',
       'A.Ramakrishnan', 'Kanniah.T', 'Alagappan Pl', 'Palanichamy C',
       'Pandiyan M.', 'Selvam K', 'Nagarajan B', 'Hariharan R',
       'Shanmugam K', 'Muniasamy A.', 'Pandi. V'], dtype=object)
>>> print(pd.unique(record['Candidate']))

Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(pd.unique(record['Candidate']))
NameError: name 'record' is not defined
>>> n = len(pd.unique(df['PMK Votes']))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    n = len(pd.unique(df['PMK Votes']))
NameError: name 'df' is not defined
>>> n = len(pd.unique(data['PMK Votes']))
>>> n
226
>>> n = len(pd.unique(data['Position']))
>>> n
12
>>> n = len(pd.unique(data['Candidate']))
>>> n
230
>>> n = len(pd.unique(data['Candidate'].max()))
>>> n
1
>>> print(len(pd.unique(data['Candidate'].max())))
1
>>> print(pd.unique(data['Candidate'].max()))
['Vinoth.V']
>>> print(pd.unique(data['Position'].max()))
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(pd.unique(data['Position'].max()))
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\algorithms.py", line 429, in unique
    table = htable(len(values))
TypeError: len() of unsized object
>>> print(len(pd.unique(data['Position'].max())))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(len(pd.unique(data['Position'].max())))
  File "C:\Users\Asus\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pandas\core\algorithms.py", line 429, in unique
    table = htable(len(values))
TypeError: len() of unsized object
>>> print(len(pd.unique(data['Candidate'].min())))
1
>>> print(pd.unique(data['Candidate'].min()))
['A.Adhikesavan']
>>> print(pd.unique(data['PMK Votes'].min()))
['1,007']
>>> print(pd.unique(data['PMK Votes'].max()))
['950']
>>> d=data.Position.nunique()
>>> d
12
>>> g= data.groupby(['PMK Votes']).sum() 

>>> g
             #      Position
PMK Votes                   
1,007          182         7
1,011          139         6
1,025          156         6
1,036          150         6
1,045          178         7
...            ...       ...
9,339          116         5
9,586           41         3
9,736           81         4
927            146         6
950            163         6

[226 rows x 2 columns]
>>> g= data.groupby(['PMK Votes']).count()
>>> g
             #      Position  Candidate  ...  Total Votes  Turnout  PMK Votes %
PMK Votes                                ...                                   
1,007            1         1          1  ...            1        1            1
1,011            1         1          1  ...            1        1            1
1,025            1         1          1  ...            1        1            1
1,036            1         1          1  ...            1        1            1
1,045            1         1          1  ...            1        1            1
...            ...       ...        ...  ...          ...      ...          ...
9,339            1         1          1  ...            1        1            1
9,586            1         1          1  ...            1        1            1
9,736            1         1          1  ...            1        1            1
927              1         1          1  ...            1        1            1
950              1         1          1  ...            1        1            1

[226 rows x 8 columns]
>>> 