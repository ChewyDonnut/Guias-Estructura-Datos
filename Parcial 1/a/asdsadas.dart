import 'dart:io';
import 'dart:math';

void main() {
  List<int> lista1 = [];
  List<int> lista2 = [];
  List<int> lista3 = [];
  int lista4 = 0;
  Random random = Random();

  for (int i = 1; i <= 5; i++) {
    lista1.add(random.nextInt(10) + 1);
    print("Ingresar dato $i a lista 2:");
    int numero = int.parse(stdin.readLineSync()!);
    lista2.add(numero);
  }

  lista3 = [...lista1, ...lista2]; // Concatenar lista1 y lista2

  print("Lista 1:\n$lista1");
  print("Lista 2:\n$lista2");
  print("Lista 3 (Concatenación de Lista 1 y Lista 2):\n$lista3");

  lista3.insertAll(
      7, [14, 20, 7]); // Agregar elementos en la posición 7 de lista3

  print("Lista 3 con elementos agregados en posiciones específicas:\n$lista3");
  print("Longitud de lista3: ${lista3.length}");

  for (int i = 0; i < lista3.length; i++) {
    lista4 += lista3[i];
  }

  lista4 = lista4 ~/ lista3.length; // Promedio de los elementos de lista3

  print("Promedio de los elementos de lista3: $lista4");
}
