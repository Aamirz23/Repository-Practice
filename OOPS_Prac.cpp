#include <iostream>
#include <memory>
#include <string>
using namespace std;

class Student {
private:
  string name;
  int age;

public:
  Student(const string Name, int Age) : name(Name), age(Age) {};

  string getName() {
    return name;
  }

  void setName(string Name) {
    name = Name;
  }

  void info() const {
    cout << "Hello! My name is " << name << " and my age is " << age << endl;
  };

  virtual void greetings() { cout << "Good morning Teacher!" << endl; };

  virtual ~Student() = default;
};

class Teacher : public Student {
private:
public:
  Teacher(const string &Name, int Age) : Student(Name, Age) {}
  
  void greetings() override {
    cout << "Good Morning students, I am your new teacher!" << endl;
  };

  void askInfo(const Student &student) {
    cout << "Introduce Yourself " << endl;
    student.info();
  }
};

int main() {
  auto(S1) = make_unique<Student>("James", 18);
  auto(T1) = make_unique<Teacher>("Mason", 27);
  unique_ptr<Student> S2 = make_unique<Student>("Masood", 29);
  cout << "*****CLASSROOM*****" << endl;
  S1->greetings();
  T1->greetings();
  T1->askInfo(*S1);
  cout << S2->getName() << endl;
  S2->setName("Mujtaba");
  cout << S2->getName() << endl;
}
