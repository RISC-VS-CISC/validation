cp load_bitstream.tcl bitstream.tcl
sed -i "s/{bit_stream_file}/$1/" bitstream.tcl
$Vivado_path -mode tcl -script bitstream.tcl
rm ./bitstream.tcl
rm ./vivado*