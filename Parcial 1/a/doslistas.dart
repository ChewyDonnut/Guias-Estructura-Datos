import 'dart:io';
import 'dart:math';

void main() {
  List<int> lista1 = [];
  List<int> lista2 = [];
  List<int> lista3 = [];
  double promedio = 0;
  Random random = Random();
  for (int i = 1; i <= 5; i++) {
    lista1.add(random.nextInt(10) + 1);
    print("ingresar dato $i a lista 2 ");
    int numero = (int.parse(stdin.readLineSync()!)).truncate();
    lista2.add(numero);
  }
  lista3 = lista1 + lista2;
  print("lista 1:\n" + "$lista1");
  print("lista 2:\n" + "$lista2");
  print("lista 3:\n" + "$lista3");
  lista3.insertAll(7, [14, 20, 7]);
  print("lista 3:\n" + "$lista3");
  print(lista3.length);
  for (int i = 0; i < lista3.length; i++) {
    promedio += lista3[i];
  }
  promedio = (promedio / lista3.length);
  print(promedio);
  lista3.sort();
  print(lista3.reversed);
}
