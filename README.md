# SmartCushion

## Installation Instructions

### Prerequisites

1. Ensure you have access to the application source code.
2. Install Node.js on your machine.

### Setup

1. Navigate to the `smartcushion/cushionv3` directory in your terminal.
2. Run the following commands:

   ```bash
   npm install
   npm install -g expo-cli
   npx expo start
   ```

3. The application should now be running.

### Running the Application

1. Install the Expo Go application on your smartphone.
2. Scan the provided QR code or use an Android simulator on your computer to view the application.

## Configuration

### Adjusting Sedentary and Bad Posture Timers

To change the sedentary time and bad posture time settings, follow these steps:

1. Navigate to the following file:
   ```
   /app/(drawer)/Home/index.js
   ```
2. Locate the comments next to each timer and make your desired changes.

### Flask API Configuration

The Flask API is configured in several files. Each configuration has a corresponding comment for easy identification:

1. `/app/(drawer)/EnvData/index.js`
2. `/app/(drawer)/Home/index.js`
3. `/app/HistoryData/DailyView.js`
4. `/app/HistoryData/WeeklyView.js`
5. `/app/HistoryData/MonthlyView.js`
6. `/app/HistoryData/SelectDateView.js`

Make sure to update the API configurations as needed in the respective files.
