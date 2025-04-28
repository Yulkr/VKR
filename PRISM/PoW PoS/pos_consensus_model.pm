
const int MAX = 10;
const double stake = 0.6;

module pos_consensus
  steps : [0..MAX] init 0;
  honest : [0..MAX] init 0;
  attack : [0..MAX] init 0;

  [] steps < MAX & honest < MAX & attack < MAX ->
     stake       : (steps' = steps + 1) & (attack' = attack + 1) +
     (1 - stake) : (steps' = steps + 1) & (honest' = honest + 1);
endmodule

label "attack_majority" = attack > honest;
label "honest_majority" = honest > attack;
label "equal" = attack = honest;
