`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04.07.2026 14:50:12
// Design Name: 
// Module Name: VotingMachine
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module VotingMachine(
input clock,
input reset,
input mode,
input button1,
input button2,
input button3,
input button4,
output[7:0] led
    );
    
    wire valid_vote_1;
    wire valid_vote_2;
    wire valid_vote_3;
    wire valid_vote_4;
    
buttoncontrol bc1(
.clock(clock),
.reset(reset),
.button(button1),
.valid_vote(valid_vote_1)
    );
    
    
    
 buttoncontrol bc2(
.clock(clock),
.reset(reset),
.button(button2),
.valid_vote(valid_vote_2)
    );    
    
 buttoncontrol bc3(
.clock(clock),
.reset(reset),
.button(button3),
.valid_vote(valid_vote_3)
    );    
 
   
 buttoncontrol bc4(
.clock(clock),
.reset(reset),
.button(button4),
.valid_vote(valid_vote_4)
    );    
    
    
    

voteLogger VL(
.clock(clock),
.reset(reset),
.cand1_vote_valid(valid_vote_1),
.cand2_vote_valid(valid_vote_2),
.cand3_vote_valid(valid_vote_3),
.cand4_vote_valid(valid_vote_4),
.cand1_vote_recvd(),
.cand2_vote_recvd(),
.cand3_vote_recvd(),
.cand4_vote_recvd()

    );
endmodule
