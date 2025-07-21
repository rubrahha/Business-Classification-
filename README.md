# Business-Classification-

---

## 🔧 Tools & Technologies Used

- **Languages**: Python, SQL (conceptually)
- **Libraries**: Pandas, NumPy, Regex, Requests
- **Platforms**: Jupyter Notebook, VS Code
- **Visualization**: Tableau / Power BI / Looker Studio
- **Version Control**: Git

---

## 🎯 Objectives

1. Load and clean raw business data (name, description, website).
2. Use **Regex** to classify each business into an industry (Retail, IT, etc.).
3. (Optional) Use **Clearbit API** or others to classify based on website domain.
4. Simulate **funnel behavior**: Visited → Signed Up → Purchased.
5. Export and visualize results in Tableau/Power BI.

---

## 🚀 How to Run

### 🖥️ 1. Clone and Setup

```bash
git clone https://github.com/yourusername/business-classification-project.git
cd business-classification-project
pip install -r requirements.txt


Business_Name,Description,Website
FreshMart,"Organic grocery store","www.freshmart.com"
CodeNinja,"Software development services","www.codeninja.io"
HappyPaws,"Pet grooming and accessories","www.happypaws.net"



| Business\_Name | Description                   | Website                                       | Industry      | Visited | Signed\_Up | Purchased |
| -------------- | ----------------------------- | --------------------------------------------- | ------------- | ------- | ---------- | --------- |
| FreshMart      | organic grocery store         | [www.freshmart.com](http://www.freshmart.com) | Food & Retail | 1       | 1          | 1         |
| CodeNinja      | software development services | [www.codeninja.io](http://www.codeninja.io)   | IT Services   | 1       | 0          | 0         |
| HappyPaws      | pet grooming and accessories  | [www.happypaws.net](http://www.happypaws.net) | Pet Services  | 1       | 1          | 0         |
