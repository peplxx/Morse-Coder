module keyboardDriver (
	input clk, 
	input [3:0] col,
	output reg [3:0] row, 
	output reg [7:0] keyCode
);

reg [1:0]state=2'b00;
reg [1:0]nextState=2'b00;

integer i;
integer cnt=0;

integer DELAY = 10;
integer ticks = 0;

reg [7:0] buff = 8'b00000000;


//state register
always@(posedge clk) begin
	if (ticks == DELAY)begin
    state <= nextState;
	 ticks = 0;
	end
	else begin
		ticks = ticks + 1;
	end
end

// Cha
always@(posedge clk) begin
	case (state)
		2'b00: row <= 4'b1110;
		2'b01: row <= 4'b1101;
		2'b10: row <= 4'b1011;
		2'b11: row <= 4'b0111;
		default: row <= 4'b1110;
	endcase
	 cnt = 0;
	 buff <= {~row[0],~row[1],~row[2],~row[3], ~col[0],~col[1],~col[2],~col[3]};
	 for (i = 0;i<8;i = i+1)begin
		if (buff[i])begin
			cnt = cnt+1;
		end
	 end
	 if (~col != 4'b0000 && cnt == 2)begin
		 keyCode <= {~row[0],~row[1],~row[2],~row[3], ~col[0],~col[1],~col[2],~col[3]};
		 
	 end
end

// Next state
always @(posedge clk) begin
        case (state)
            2'b00: nextState <= 2'b01;
            2'b01: nextState <= 2'b10;
            2'b10: nextState <= 2'b11;
            2'b11: nextState <= 2'b00;
            default: nextState <= 2'b00;
        endcase
end
endmodule