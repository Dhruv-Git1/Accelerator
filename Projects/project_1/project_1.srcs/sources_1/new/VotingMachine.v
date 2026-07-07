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
output wire [7:0] led
    );
    
    wire valid_vote_1;
    wire valid_vote_2;
    wire valid_vote_3;
    wire valid_vote_4;
    wire [7:0] cand1_vote_recvd;
    wire [7:0] cand2_vote_recvd;
    wire [7:0] cand3_vote_recvd;
    wire [7:0] cand4_vote_recvd;
    
    wire anyValidVote;
    
    assign anyValidVote= valid_vote_1 || valid_vote_2 || valid_vote_3 || valid_vote_4;
    
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

modecontrol MC(
.clock(clock),
.reset(reset),
.mode(mode),
.valid_vote_casted(anyValidVote), //if one of them gots valid vote, it gets high candivate1_vote,
.candidate1_vote(cand1_vote_recvd),
.candivate2_vote(cand2_vote_recvd),
.candivate3_vote(cand3_vote_recvd),
.candivate4_vote(cand4_vote_recvd),
.candidate1_butto_press(valid_vote_1),
.candidate2_butto_press(valid_vote_2),
.candidate3_butto_press(valid_vote_3),
.candidate4_butto_press(valid_vote_4),
.leds(led)

    );
endmodule
