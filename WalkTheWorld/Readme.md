# Walk the World: Analyzing Walkable Routes Across Cities

This project explores the possibility of walking between two cities without crossing an ocean and calculates the shortest route in terms of border crossings. It combines web scraping, graph traversal, and data extraction techniques to provide insights into geography and route planning.

## Project Overview

- **Objective**: Determine if two cities are walkable, find the shortest route, and provide information about the countries along the way.
- **Features**:
  - Validate city existence using Wikipedia.
  - Extract country and continent data.
  - Identify whether cities are separated by oceans.
  - Compute the shortest route using graph traversal.
  - Retrieve country-specific statistics (area, population, GDP).

---

## Technologies Used

**Programming Language**: Python

**Libraries**:
- **Web Scraping**: `requests`, `BeautifulSoup`, `lxml`
- **Graph Traversal**: `collections` (deque)
- **Data Extraction**: XPath, CSS selectors
- **Data Representation**: HTML parsing, Wikipedia infobox data

---

## Features

### 1. Input Validation
- Verifies if the given cities exist on Wikipedia using BeautifulSoup.
- Returns an error message if no valid Wikipedia page is found.

### 2. Country and Continent Extraction
- Extracts the country each city belongs to using CSS selectors and XPath.
- Checks if the cities are in the same country or located on different continents.

### 3. Ocean Separation
- Determines whether the cities are separated by an ocean based on continent mappings and predefined ocean-separation logic.

### 4. Shortest Route Calculation
- Uses BFS (Breadth-First Search) to calculate the route with the minimum number of border crossings.
- Constructs a graph of countries and their neighbors using Wikipedia’s "List of countries and territories by number of land borders."

### 5. Country Information
- For each country in the route, retrieves:
  - Total area
  - Population
  - GDP per capita
- Identifies the largest, most populous, and richest countries along the route.

---

## Folder Structure
walk_the_world/ ├── walk_the_world.ipynb # Jupyter notebook containing all code and explanations ├── README.md # Project overview

---

## Key Insights

1. **Walkable Routes**:
   - Determines routes with minimal border crossings for intercontinental travel.
   - Handles cases where cities are separated by oceans and terminates with appropriate messages.

2. **Geographic Insights**:
   - Identifies landlocked and ocean-separated regions.
   - Extracts comprehensive data on countries' geographic and economic metrics.

3. **Shortest Route**:
   - For "Tehran" to "Paris," the shortest route is:
     ```
     Tehran -> Azerbaijan -> Russia -> Poland -> Germany -> France
     ```

---

## Future Enhancements

- Expand the analysis to account for islands and ferries (e.g., island-to-mainland connections).
- Add visualization for the route map.
- Integrate economic and demographic analysis for all countries traversed.

---
