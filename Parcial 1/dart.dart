import 'dart:io';
import 'dart:math';

void main() {
  Random random = Random();
  List<int> lista1 = [];
  List<int> lista2 = [];
  double prom = 0;
  for (int i = 1; i <= 5; i++) {
    lista1.add(-100 + random.nextInt(200));
    print("ingresa dato numro $i");
    lista2.add(int.parse(stdin.readLineSync()!));
  }
  print("lista1");
  print(lista1);
  print("lista2");
  print(lista2);
  List<int> lista3 = lista1 + lista2;
  print("lista concatenada");
  print(lista3);

  lista3.insertAll(6, [14, 20, 7]);
  print("lista concatenada con datos agregados");
  print(lista3);
  lista3.sort();
  print("lista ordenada");
  print(lista3.reversed);
  for (int i = 0; i < lista3.length; i++) {
    prom += lista3[i];
  }
  print(prom / lista3.length);
}
