const canvas = document.querySelector('canvas');
const winRate = canvas.getAttribute('win-rate');
var ctx = document.getElementById('win-rate-chart-1').getContext('2d');

new Chart(ctx, {
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