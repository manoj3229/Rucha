*** Settings ***
Library     Collections

*** Variables ***
[Arguments]     ${val}  ${String}   ${Str}  ${palindromStr}


*** Test Cases ***
Even or Odd

    ${result}=    Evaluate    ${val} % 2

    IF  ${result} == 0
        Log To Console   ${val} is Even
    ELSE
        Log To Console   ${val} is Odd
    END

Reverse the String
    ${reverse}=     Evaluate    "${String}"[::-1]
    Log To Console  ${reverse}

Count characters in String
    ${counter}=   Evaluate  collections.Counter("${Str}")
    Log To Console  ${counter}

Find largest number
    @{list}=    Create List     10  20  67  80  30  3   90
    ${largest}=     Evaluate    max(@{list})
    Log To Console  ${largest}

Find largest number by sorting
    @{listToSort}=    Create List    10    50    55    60    80    157    85
    ${newList}=     Evaluate    sorted([int(x) for x in ${listToSort}])
    ${large}=   Get From List   ${newList}     -1   
    Log To Console  ${large}

Palindrome Check
    ${rev}=     Evaluate   "${palindromStr}"[::-1]
    
    IF      '${palindromStr}'=='${rev}' 
        Log To Console      Palindrome
    ELSE
        Log To Console      Not Palindrome
    END



