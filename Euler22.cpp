// CSC 160 Project Euler 22
// Ethan Bond 
// 8/2/2019
// Reads names from a text file and then creates a score based on alphabetical rank and letter index

#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

// Prototype the bubbleSort function
void bubbleSort(string arr[], int size);

int main()
{
  // Hold a constant that is the number of names in the textfile
  const int SIZE = 5163;
  int letterSum, count, finalScore = 0;

  // declare string variables. allNames will be used to store all of the names
  // letterReference will be used to check the index of a leter 
  string line, nextName, allNames[SIZE], letterReference = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  // Create an input filestream for the textfile of names 
  ifstream inFile("p022_names.txt");

  // Make sure that the file opened corrrectly, display to the user if not
  if(!inFile.is_open())
  {
    cout << "Error opening file" << endl;
  }


  // All of the names are written in a single line in the text file
  getline(inFile,line);
  stringstream namesStream(line);

  // Take each name from the text file and add it to the array of names
  for(int nameIndex=0;nameIndex<SIZE;nameIndex++)
  {
    getline(namesStream, nextName, ',');
    allNames[nameIndex] = nextName.substr(1,nextName.length()-2);
  }

  // Use the bubblesort function to sort the names alphabetically
  bubbleSort(allNames,SIZE);

  // Count will be used to determine the names' rank in the array
  count = 0;
  for(string name:allNames)
  {
    count++;
    letterSum = 0;
    
    // Sum all of the indexes of the letters 
    for(int letterIndex=0;letterIndex<name.length();letterIndex++){
      letterSum += letterReference.find(name[letterIndex]);
    }

    // add the product of the name's rank and letter sum to the final score
    finalScore += count * letterSum; 
  }

  // Display the final answer to the user 
  cout << "Final Answer: " << finalScore << endl;

  return 0;
}

void bubbleSort(string arr[], int size)
{
  // Need a string that will be used temporarily to store the value that is being swapped
  string temp;
  bool sorted = false;
  while(!sorted)
  {
    // Initialize sorted to true
    sorted = true;
    for (int index=0;index<size-1;index++)
    {
      if(arr[index]>arr[index+1])
      {
        // Swap the strings if they don't follow the order rules, turn sorted to false
        sorted = false;
        temp = arr[index];
        arr[index] = arr[index+1];
        arr[index+1] = temp;
      }
    }
  }
}