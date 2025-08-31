# https://docs.python.org/3/library/re.html

import re

report_snapshot = '''<?xml version="1.0" encoding="UTF-8"?>
<ReportSnapshot Major="1" Minor="0" Revision="1">
	<CoIDs>
		<CoID Type="RepNo">0147N</CoID>
		<CoID Type="CompanyName">Advanced Micro Devices Inc</CoID>
		<CoID Type="IRSNo">941692300</CoID>
		<CoID Type="CIKNo">0000002488</CoID>
		<CoID Type="OrganizationPermID">4295903297</CoID>
	</CoIDs>
	<Issues>
		<Issue ID="1" Type="C" Desc="Common Stock" Order="1">
			<IssueID Type="Name">Ordinary Shares</IssueID>
			<IssueID Type="Ticker">AMD</IssueID>
			<IssueID Type="RIC">AMD.O</IssueID>
			<IssueID Type="DisplayRIC">AMD.OQ</IssueID>
			<IssueID Type="InstrumentPI">258697</IssueID>
			<IssueID Type="QuotePI">1089490</IssueID>
			<IssueID Type="InstrumentPermID">8590934144</IssueID>
			<IssueID Type="QuotePermID">55838319834</IssueID>
			<Exchange Code="NASD" Country="USA">NASDAQ</Exchange>
			<GlobalListingType>OSR</GlobalListingType>
			<MostRecentSplit Date="2000-08-22">2.0</MostRecentSplit>
		</Issue>
	</Issues>
	<CoGeneralInfo>
		<CoStatus Code="1">Active</CoStatus>
		<CoType Code="EQU">Equity Issue</CoType>
		<LastModified>2025-08-06</LastModified>
		<LatestAvailableAnnual>2024-12-28</LatestAvailableAnnual>
		<LatestAvailableInterim>2025-06-28</LatestAvailableInterim>
		<Employees LastUpdated="2024-12-28">28000</Employees>
		<SharesOut Date="2025-07-30" TotalFloat="1614630323.0">1622843689.0</SharesOut>
		<ReportingCurrency Code="USD">U.S. Dollars</ReportingCurrency>
		<MostRecentExchange Date="2025-08-19">1.0</MostRecentExchange>
	</CoGeneralInfo>
	<TextInfo>
		<Text Type="Business Summary" lastModified="2025-08-02T14:49:17">Advanced Micro Devices, Inc. is a global semiconductor company. The Company is focused on high-performance computing, graphics and visualization technologies. Its segments include Data Center, Client and Gaming, and Embedded. Data Center segment includes artificial intelligence (AI) accelerators, microprocessors (CPUs) for servers, graphics processing units (GPUs), accelerated processing units (APUs), data processing units (DPUs), Field Programmable Gate Arrays (FPGAs), smart network interface Cards (SmartNICs) and Adaptive system-on-Chip (SoC) products for data centers. Client and Gaming segment includes CPUs, APUs, chipsets for desktops and notebooks, discrete GPUs, and semi-custom SoC products and development services. Embedded segment includes embedded CPUs, GPUs, APUs, FPGAs, system on modules (SOMs), and Adaptive SoC products. It markets and sells its products under the AMD trademark. Its products include AMD EPYC, AMD Ryzen, AMD Ryzen PRO, Virtex UltraScale+, and others.</Text>
		<Text Type="Financial Summary" lastModified="2025-08-06T14:26:57"> BRIEF: For the 26 weeks ended 28 June 2025, Advanced Micro Devices Inc revenues increased 34% to $15.12B. Net income before extraordinary items increased from $388M to $1.48B. Revenues reflect Client segment increase of 68% to $4.79B, Data Centre segment increase of 34% to $6.91B, Gaming segment increase of 13% to $1.77B. Net income benefited from All Other segment loss decrease of 5% to $1.97B.</Text>
	</TextInfo>
	<contactInfo lastUpdated="2025-08-20T03:53:59">
		<streetAddress line="1">2485 Augustine Drive</streetAddress>
		<streetAddress line="2"></streetAddress>
		<streetAddress line="3"></streetAddress>
		<city>SANTA CLARA</city>
		<state-region>CA</state-region>
		<postalCode>95054</postalCode>
		<country code="USA">United States</country>
		<contactName></contactName>
		<contactTitle></contactTitle>
		<phone>
			<phone type="mainphone">
				<countryPhoneCode>1</countryPhoneCode>
				<city-areacode>408</city-areacode>
				<number>7494000</number>
			</phone>
			<phone type="mainfax">
				<countryPhoneCode>1</countryPhoneCode>
				<city-areacode>302</city-areacode>
				<number>6555049</number>
			</phone>
		</phone>
	</contactInfo>
	<webLinks lastUpdated="2024-11-18T07:34:46"><webSite mainCategory="Home Page">https://www.amd.com/</webSite><eMail mainCategory="Company Contact/E-mail">Investor.Relations@amd.com</eMail></webLinks>
	<peerInfo lastUpdated="2025-08-20T03:53:59">
		<IndustryInfo>
			<Industry type="TRBC" order="1" reported="0" code="5710101010" mnem="">Semiconductors (NEC)</Industry>
			<Industry type="NAICS" order="1" reported="0" code="334413" mnem="">Semiconductor and Related Device Manufacturing</Industry>
			<Industry type="NAICS" order="2" reported="0" code="423690" mnem="">Other Electronic Parts and Equipment Merchant Wholesalers</Industry>
			<Industry type="NAICS" order="3" reported="0" code="513210" mnem="">Software Publishers</Industry>
			<Industry type="NAICS" order="4" reported="0" code="334111" mnem="">Electronic Computer Manufacturing</Industry>
			<Industry type="SIC" order="0" reported="1" code="3674" mnem="">Semiconductors/related Devices</Industry>
			<Industry type="SIC" order="1" reported="0" code="3674" mnem="">Semiconductors/related Devices</Industry>
			<Industry type="SIC" order="2" reported="0" code="5065" mnem="">Electronic Parts And Equipment</Industry>
			<Industry type="SIC" order="3" reported="0" code="7372" mnem="">Prepackaged Software</Industry>
			<Industry type="SIC" order="4" reported="0" code="3571" mnem="">Electronic Computers</Industry>
		</IndustryInfo>
		<Indexconstituet>S&amp;P 500</Indexconstituet>
	</peerInfo>
	<officers>
		<officer rank="1" since="01/2012">
			<firstName>Lisa</firstName>
			<mI>T.</mI>
			<lastName>Su</lastName>
			<age>55 </age>
			<title startYear="2024" startMonth="08" startDay="30" iD1="CHM" abbr1="Chmn." iD2="PRE" abbr2="Pres.">Chairman of the Board, Chief Executive Officer, President, Executive Director</title>
		</officer>
		<officer rank="2" since="01/23/2023">
			<firstName>Jean</firstName>
			<mI></mI>
			<lastName>Hu</lastName>
			<age>61 </age>
			<title startYear="2023" startMonth="01" startDay="23" iD1="CFO" abbr1="CFO" iD2="EVP" abbr2="Exec. VP">Chief Financial Officer, Executive Vice President, Treasurer</title>
		</officer>
		<officer rank="3" since="10/24/2011">
			<firstName>Mark</firstName>
			<mI>D.</mI>
			<lastName>Papermaster</lastName>
			<age>63 </age>
			<title startYear="2019" startMonth="01" startDay="" iD1="EVP" abbr1="Exec. VP" iD2="CTO" abbr2="CTO">Chief Technology Officer, Executive Vice President - Technology and Engineering</title>
		</officer>
		<officer rank="4" since="10/2014">
			<firstName>Forrest</firstName>
			<mI>Eugene</mI>
			<lastName>Norrod</lastName>
			<age>59 </age>
			<title startYear="2022" startMonth="" startDay="" iD1="EVP" abbr1="Exec. VP" iD2="GMG" abbr2="GM">Executive Vice President, General Manager - Data Center Solutions Business Unit</title>
		</officer>
		<officer rank="5" since="01/2019">
			<firstName>Darren</firstName>
			<mI></mI>
			<lastName>Grasby</lastName>
			<age>54 </age>
			<title startYear="2025" startMonth="01" startDay="" iD1="EVP" abbr1="Exec. VP" iD2="" abbr2="">Executive Vice President, Chief Sales Officer</title>
		</officer>
		<officer rank="6" since="06/2023">
			<firstName>Philip</firstName>
			<mI></mI>
			<lastName>Guido</lastName>
			<age>63 </age>
			<title startYear="2023" startMonth="06" startDay="" iD1="EVP" abbr1="Exec. VP" iD2="" abbr2="">Executive Vice President, Chief Commercial Officer</title>
		</officer>
		<officer rank="7" since="01/22/2024">
			<firstName>Ava</firstName>
			<mI>M.</mI>
			<lastName>Hahn</lastName>
			<age>52 </age>
			<title startYear="2024" startMonth="01" startDay="22" iD1="SVP" abbr1="Sr. VP" iD2="GCN" abbr2="Counsel">Senior Vice President, General Counsel, Corporate Secretary</title>
		</officer>
		<officer rank="8" since="04/2023">
			<firstName>Jack</firstName>
			<mI></mI>
			<lastName>Huynh</lastName>
			<age>46 </age>
			<title startYear="2023" startMonth="04" startDay="" iD1="SVP" abbr1="Sr. VP" iD2="GMG" abbr2="GM">Senior Vice President, General Manager - Computing and Graphics Business Group</title>
		</officer>
	</officers>
	<Ratios PriceCurrency="USD" ReportingCurrency="USD" ExchangeRate="1.00000" LatestAvailableDate="2025-06-28">
		<Group ID="Price and Volume">
			<Ratio FieldName="NPRICE" Type="N">165.20000</Ratio>
			<Ratio FieldName="NHIG" Type="N">186.65000</Ratio>
			<Ratio FieldName="NLOW" Type="N">76.48000</Ratio>
			<Ratio FieldName="PDATE" Type="D">2025-08-20T00:00:00</Ratio>
			<Ratio FieldName="VOL10DAVG" Type="N">67.40846</Ratio>
			<Ratio FieldName="EV" Type="N">265444.80000</Ratio>
		</Group>
		<Group ID="Income Statement">
			<Ratio FieldName="MKTCAP" Type="N">268093.80000</Ratio>
			<Ratio FieldName="TTMREV" Type="N">29600.00000</Ratio>
			<Ratio FieldName="TTMEBITD" Type="N">5750.00000</Ratio>
			<Ratio FieldName="TTMNIAC" Type="N">2730.00000</Ratio>
		</Group>
		<Group ID="Per share data">
			<Ratio FieldName="TTMEPSXCLX" Type="N">1.67346</Ratio>
			<Ratio FieldName="TTMREVPS" Type="N">18.14281</Ratio>
			<Ratio FieldName="QBVPS" Type="N">36.78483</Ratio>
			<Ratio FieldName="QCSHPS" Type="N">3.61714</Ratio>
			<Ratio FieldName="TTMCFSHR" Type="N">3.53478</Ratio>
			<Ratio FieldName="TTMDIVSHR" Type="N">0.00000</Ratio>
		</Group>
		<Group ID="Other Ratios">
			<Ratio FieldName="TTMGROSMGN" Type="N">47.62162</Ratio>
			<Ratio FieldName="TTMROEPCT" Type="N">4.69867</Ratio>
			<Ratio FieldName="TTMPR2REV" Type="N">9.05722</Ratio>
			<Ratio FieldName="PEEXCLXOR" Type="N">98.71763</Ratio>
			<Ratio FieldName="PRICE2BK" Type="N">4.49098</Ratio>
			<Ratio FieldName="Employees" Type="N">28000</Ratio>
		</Group>
	</Ratios>
	<ForecastData ConsensusType="Mean" CurFiscalYear="2025" CurFiscalYearEndMonth="12" CurInterimEndCalYear="2025" CurInterimEndMonth="9" EarningsBasis="PRX">
		<Ratio FieldName="ConsRecom" Type="N">
			<Value PeriodType="CURR">2.1458</Value>
		</Ratio>
		<Ratio FieldName="TargetPrice" Type="N">
			<Value PeriodType="CURR">170.26920</Value>
		</Ratio>
		<Ratio FieldName="ProjLTGrowthRate" Type="N">
			<Value PeriodType="CURR">32.3075</Value>
		</Ratio>
		<Ratio FieldName="ProjPE" Type="N">
			<Value PeriodType="CURR">42.25929</Value>
		</Ratio>
		<Ratio FieldName="ProjSales" Type="N">
			<Value PeriodType="CURR">33012.03520</Value>
		</Ratio>
		<Ratio FieldName="ProjSalesQ" Type="N">
			<Value PeriodType="CURR">8723.91440</Value>
		</Ratio>
		<Ratio FieldName="ProjEPS" Type="N">
			<Value PeriodType="CURR">3.90920</Value>
		</Ratio>
		<Ratio FieldName="ProjEPSQ" Type="N">
			<Value PeriodType="CURR">1.15900</Value>
		</Ratio>
		<Ratio FieldName="ProjProfit" Type="N">
			<Value PeriodType="CURR">6315.05140</Value>
		</Ratio>
		<Ratio FieldName="ProjDPS" Type="N">
			<Value PeriodType="CURR">0.00000</Value>
		</Ratio>
	</ForecastData>
</ReportSnapshot>'''

#"Financial Summary" lastModified="2025-08-06T14:26:57"
def main() -> None:
    fin_summary = re.findall(r'"Financial Summary"\slastModified="([0-9-]+)', report_snapshot)
    print(fin_summary)

if __name__ == '__main__':
    main()
