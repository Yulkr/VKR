
// Дискретная стохастическая модель гонки между атакующим и честными узлами
const double q = 0.6;
//const double q;
dtmc

module pow_consensus
  a : [0..20] init 0;  // блоки атакующего
  h : [0..20] init 0;  // блоки честных узлов

  [] a < 20 & h < 20 ->
     q       : (a' = a + 1) +
     (1 - q) : (h' = h + 1);
endmodule

label "attack_success" = a >= h;
label "attack_fail" = h >= a + 5;
