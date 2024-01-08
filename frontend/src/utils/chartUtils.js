import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Survey Results',
    },
  },
};

export function prepareBarChartData(data) {
  const labels = data.map(item => item.label);
  const dataset = data.map(item => item.value);

  return {
    labels,
    datasets: [
      {
        label: 'Responses',
        data: dataset,
        backgroundColor: 'rgba(53, 162, 235, 0.5)',
      },
    ],
  };
}

export function BarChart({ data }) {
  const chartData = prepareBarChartData(data);
  return <Bar options={options} data={chartData} />;
}