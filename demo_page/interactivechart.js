	d3.csv("choreos.csv", function(error,dataChoreo) {
		if (error) {
			console.log(error);
		} else {
			var dsv = d3.dsv("|","text/plain");
			dsv("pieces.csv", function(error,dataPiece) {
				if (error) {
					console.log(error);
				} else {

					var choreosvg = d3.select("#svgPieceChoreo")
					h = 500;
					w = 1000;
					choreosvg.attr("width",w).attr("height",h);


					var counts = dataChoreo.map(function(o){
						return parseInt(o.count);
					});
					var choreographers = dataChoreo.map(function(o){
						return o.choreographer;
					});
					var count = counts.reduce(function(a, b) {
						return a+b;
					});

					var choreodata = dataChoreo.map(function(o){
						return [o.choreographer,parseInt(o.count)];
					});
					var thischoreodata = choreodata.slice(0,25);


					var countsPiece = dataPiece.map(function(o){
						return o.count
					});
					var countPiece = countsPiece.reduce(function(a, b) {
						return parseInt(a) + parseInt(b);
					});

					var piecedata = dataPiece.map(function(o){
						return [o.piece,parseInt(o.count)];
					})

					var thispiecedata = piecedata.slice(0,25);


					var max_data_choreo = d3.max(thischoreodata, function(d){return d[1];});
					var min_data_choreo = d3.min(thischoreodata, function(d){return d[1];});
					var yScaleChoreo = d3.scale.linear()
					.domain([0,max_data_choreo])
					.range ([0,h]);
					var yScaleReversedChoreo = d3.scale.linear()
					.domain([0,max_data_choreo])
					.range ([h,0]);
					var xScaleChoreo = d3.scale.linear()
					.domain([0,thischoreodata.length])
					.range([0,w]);
					var xScaleReversedChoreo = d3.scale.linear()
					.domain([0,thischoreodata.length])
					.range([w,0]);
					var colorScaleChoreo = d3.scale.sqrt()
					.domain([0,max_data_choreo])
					.rangeRound([50,200]);
					var xOrdinalScaleChoreo = d3.scale.ordinal()
					.domain(d3.range(thischoreodata.length))
					.rangeRoundBands([0,w],0.05);


					var max_data_pieces = d3.max(thispiecedata, function(d){return d[1];});
					var min_data_pieces = d3.min(thispiecedata, function(d){return d[1];});
					var yScalePiece = d3.scale.linear()
					.domain([0,max_data_pieces])
					.range ([0,h]);
					var yScaleReversedPiece = d3.scale.linear()
					.domain([0,max_data_pieces])
					.range ([h,0]);
					var xScalePiece = d3.scale.linear()
					.domain([0,thispiecedata.length])
					.range([0,w]);
					var xScaleReversedPiece = d3.scale.linear()
					.domain([0,thispiecedata.length])
					.range([w,0]);
					var colorScalePiece = d3.scale.sqrt()
					.domain([0,max_data_pieces])
					.rangeRound([50,200]);
					var xOrdinalScalePiece = d3.scale.ordinal()
					.domain(d3.range(thispiecedata.length))
					.rangeRoundBands([0,w],0.05);


					var rects = choreosvg.selectAll("rect")
					.data(thischoreodata)
					.enter()
					.append("rect")
					.attr({
						x: function(d,i) { return xOrdinalScaleChoreo(i);},
						y: function(d) { return h - yScaleChoreo(d[1]);},
						width: xOrdinalScaleChoreo.rangeBand(),
						height: function(d) { return yScaleChoreo(d[1]); },
						fill: function(d) { return  "rgb(0, 0, " + colorScaleChoreo(d[1]) + ")";}
					});

					var texts = choreosvg.selectAll("text")
					.data(thischoreodata)
					.enter()
					.append("text")
					.text(function(d) {
						return d[1];
					})
					.attr({
						x: function(d,i) { return xOrdinalScaleChoreo(i)+xOrdinalScaleChoreo.rangeBand() / 2;},
						y: function(d) { return h - yScaleChoreo(d[1])+14; },
						"font-size": "11px",
						fill: "white",
						"text-anchor": "middle"
					});

					var titletext = choreosvg.append("text")
											 .text("Top " + thischoreodata.length + " Choreographers")
											 .attr({
											 	x: w-400,
											 	y: 50,
												"font-size": "30px",
												fill: "navy"
											 });

					var infodetails = choreosvg.append("text")
										.text("")
										.attr({
												x: w-400,
											 	y: 85,
											 	width: "350px",
												"font-size": "20px",
												fill: "navy"				
										});

					var onChoreos = true;

					titletext.on("click", function() {

						if (onChoreos){

						choreosvg.selectAll("rect")
						.data(thispiecedata)
						.transition()
						.delay(function(d,i){return i*50;})
						.duration(250)
						.attr("y",function(d){
							return h-yScalePiece(d[1]);
						})
						.attr("height",function(d){
							return yScalePiece(d[1]);
						})
						.attr("fill", function(d) {
							return "rgb(" + colorScalePiece(d[1]) + ",0,0)";
						});

						choreosvg.selectAll("text")
						.data(thispiecedata)
						.transition()
						.delay(function(d,i){return i*50;})
						.duration(250)
						.text(function(d) {
							return d[1];
						})
						.attr("x", function(d,i) {
							return xOrdinalScalePiece(i) + xOrdinalScalePiece.rangeBand()/2;
						})
						.attr("y", function(d) {
							return h - yScalePiece(d[1])+14;
						});

						titletext.transition()
								 .delay(250)
								 .duration(250)
								 .text("Top " + thispiecedata.length + " Ballets")
								 .attr("fill", "maroon");

						onChoreos = false;

					} else {


						choreosvg.selectAll("rect")
						.data(thischoreodata)
						.transition()
						.delay(function(d,i){return i*50;})
						.duration(250)
						.attr("y",function(d){
							return h-yScaleChoreo(d[1]);
						})
						.attr("height",function(d){
							return yScaleChoreo(d[1]);
						})
						.attr("fill", function(d) {
							return "rgb(0,0," + colorScaleChoreo(d[1]) + ")";
						});

						choreosvg.selectAll("text")
						.data(thischoreodata)
						.transition()
						.delay(function(d,i){return i*50;})
						.duration(250)
						.text(function(d) {
							return d[1];
						})
						.attr("x", function(d,i) {
							return xOrdinalScaleChoreo(i) + xOrdinalScaleChoreo.rangeBand()/2;
						})
						.attr("y", function(d) {
							return h - yScaleChoreo(d[1])+14;
						});

						titletext.transition()
								 .delay(250)
								 .duration(250)
								 .text("Top " + thischoreodata.length + " Choreographers")
								 .attr("fill", "navy");


						onChoreos = true;
					}


					}); // end of on click

				rects.on("mouseover", function(d) {
						d3.select(this)
						  .attr("fill","orange");

						var xPosition = parseFloat(d3.select(this).attr("x")) + xOrdinalScaleChoreo.rangeBand()/2;
						var yPosition = parseFloat(d3.select(this).attr("y"))/2 + h/2;

						infodetails.transition()
							.duration(50)
							.text(function(){
						  	if (onChoreos) {
						  		return d[0] + ": " + d[1] + " pieces";
						  	} else {
						  		return d[0] + ": " + d[1] + " performances";
						  	}
							})
							.attr("fill",function(){
								if (onChoreos) {
									return "navy";
								} else {
									return "maroon";
								}
							});

						infodetails.classed("hidden", false);


						}); // end of mouseover

				rects.on("mouseout", function(d) {
						 	d3.select(this)
						 	  .transition()
						 	  .duration(250)
						 	  .attr("fill", function(){
						 	  	if (onChoreos) {
						 	  		return "rgb(0,0," + colorScaleChoreo(d[1]) + ")";
						 	  	} else {
						 	  		return "rgb(" + colorScalePiece(d[1]) + ",0,0)";
						 	  	}
						 	  });
						 	infodetails.classed("hidden",true);
						 }); //end of mouseout


				} //end of inner else
			}); // end of dsv function
		} // end of outer else
	}); // end of csv function
