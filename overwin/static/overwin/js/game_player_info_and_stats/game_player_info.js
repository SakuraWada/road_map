var canvasElemants = document.querySelectorAll('canvas[id^="win-rate-chart-"]');

canvasElemants.forEach(function(canvas){

    var ctx = canvas.getContext('2d');
    const winRate = canvas.getAttribute('win-rate');
    ctx.canvas.height="100%";

    var WinRateChart = new Chart(ctx, {
        type: 'bar',
        data: {
        labels: [''],
        datasets: [{
                label: '',
                data: [winRate],
                backgroundColor: '#E0612B',
                borderWidth: 0,
            },
            {
                label: '',
                data: [100-winRate],
                backgroundColor: '#1D2539',
                borderWidth: 0,
            }
        ],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            indexAxis: 'y',
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    enabled: false
                },
            },
            scales: {
                x: {
                    max: 100,
                    stacked: true,
                    display: false,
                    ticks: {
                        display: false
                    },
                    grid: {
                        display: false
                    },
                },
                y: {
                    stacked: true,
                    display: false,
                    ticks: {
                        display: false
                    },
                    grid: {
                        display: false
                    },
                }
            },
        },
    });

    WinRateChart.canvas.parentNode.style.height = '40px';
    WinRateChart.canvas.parentNode.style.width = '110px';
});
