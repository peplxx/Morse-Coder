module keyboardScanner (
	input clk, 
	input [3:0] col,
	output reg [3:0] row, 
	output reg [7:0] keyCode);
reg [1:0]state=2'b00;
reg [1:0]nextState=2'b00;

//state register
always@(posedge clk) begin
    state <= nextState;
end

//output CL
always@(posedge clk) begin
    case (state)
    2'b00: row <= 4'b0001;
    2'b01: row <= 4'b0010;
    2'b10: row <= 4'b0100;
    2'b11: row <= 4'b1000;
    default: row <= 4'b0001;
  endcase
    if (col != 4'b0000) begin
    keyCode <= {row[0],row[1],row[2],row[3], col[0],col[1],col[2],col[3]};
    end
end

//next state CL
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