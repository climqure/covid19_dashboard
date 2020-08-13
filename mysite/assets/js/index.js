$(function () {
	"use strict";

	// chart 1

	var ctx = document.getElementById('chart1').getContext('2d');

	var myChart = new Chart(ctx, {
		type: 'line',
		data: {
			labels: ["Mohit", "Feb", "Mar", "ApMohir", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
			datasets: [{
				label: 'New Cases',
				data: [3, 3, 8, 5, 35, 4, 6, 4, 6, 3],
				backgroundColor: '#fff',
				borderColor: "transparent",
				pointRadius: "0",
				borderWidth: 3
			}, {
				label: 'Deaths',
				data: [7, 5, 14, 7, 548, 6, 10, 6, 11, 5],
				backgroundColor: "rgba(255, 255, 255, 0.25)",
				borderColor: "transparent",
				pointRadius: "0",
				borderWidth: 1
			}]
		},
		options: {
			maintainAspectRatio: true,
			legend: {
				display: true,
				labels: {
					fontColor: '#ddd',
					boxWidth: 40
				}
			},
			tooltips: {
				displayColors: true
			},
			scales: {
				xAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: '#ddd'
					},
					gridLines: {
						display: true,
						color: "rgba(221, 221, 221, 0.08)"
					},
				}],
				yAxes: [{
					ticks: {
						beginAtZero: true,
						fontColor: '#ddd'
					},
					gridLines: {
						display: true,
						color: "rgba(221, 221, 221, 0.08)"
					},
				}]
			}

		}
	});


	// chart 2

	var ctx = document.getElementById("chart2").getContext('2d');
	var myChart = new Chart(ctx, {
		type: 'doughnut',
		data: {
			labels: ["Direct", "Affiliate", "E-mail", "Other"],
			datasets: [{
				backgroundColor: [
					"#ffffff",
					"rgba(255, 255, 255, 0.70)",
					"rgba(255, 255, 255, 0.50)",
					"rgba(255, 255, 255, 0.20)"
				],
				data: [5856, 2602, 1802, 1105],
				borderWidth: [0, 0, 0, 0]
			}]
		},
		options: {
			maintainAspectRatio: false,
			legend: {
				position: "bottom",
				display: false,
				labels: {
					fontColor: '#ddd',
					boxWidth: 15
				}
			}
			,
			tooltips: {
				displayColors: false
			}
		}
	});




});
