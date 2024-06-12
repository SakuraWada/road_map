const canvas = document.querySelector('canvas');
const winRate = canvas.getAttribute('win-rate');
var ctx = document.getElementById('win-rate-chart').getContext('2d');

new Chart(ctx, {
    type: 'bar',
    data: {
    labels: [''],
    datasets: [{
        label: '',
        data: [winRate],
        backgroundColor: 'orange',
        borderWidth: 0,
    }]
    },
    options: {
        indexAxis: 'y',
        plugins: {
            legend: {
                display: false
            }
        },
    },
    scales: {
        x: {
            max: 100,
            ticks: {
                display: false
            }
        },
        y: {
            ticks: {
                display: false
            }
        }
    },
});