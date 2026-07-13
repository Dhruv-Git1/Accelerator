module top_module( 
    input [254:0] in,
    output reg [7:0] out );
//hare krishna
    integer i;
    always @(*)
        begin
            for( i=0; i<255; i= i+1)
                begin
                    if(in[i]== 1)
                        begin
                            out= out+1;
                        end
                end
        end
endmodule
