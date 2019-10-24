import webbrowser

"""
Opens various urls in browser. Using to store and access enso-seaice resources.
Add new urls to URL list below.
Run from terminal using: python url_bookmarks.py
"""

###### URL LIST #######

# Github repository
urls = ['https://github.com/rpclancy/enso_seaice']
# Deser 2010, Sea Surface Temperature Variability: Patterns and Mechanisms
urls.append('http://www.cgd.ucar.edu/staff/cdeser/docs/deser.sstvariability.annrevmarsci10.pdf')
# Baxter 2019, How tropical Pacific surface cooling contributed to accelerated sea ice melt from 2007 to 2012 
# See fig 13.
urls.append('https://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-18-0783.1')
# Bonan 2019, Non-stationary teleconnection between the Pacific Ocean and Arctic sea ice
urls.append('https://eartharxiv.org/udnm6/')
# Wallace, On the Arctic and Antarctic Oscillations
urls.append('http://research.jisao.washington.edu/wallace/ncar_notes/')
# Multi-model large ensemble
urls.append('http://www.cesm.ucar.edu/projects/community-projects/MMLEA/')
# Tsubasa papers
urls.append('https://journals.ametsoc.org/doi/full/10.1175/JCLI-D-16-0541.1')
urls.append('https://journals.ametsoc.org/doi/full/10.1175/JCLI-D-16-0441.1')
#Olonscheck 2019, Arctic sea-ice variability is primarily driven by atmospheric temperature fluctuations
urls.append('https://www.nature.com/articles/s41561-019-0363-1')
#Kolstad 2019, Nonstationary Relationship Between Autumn Arctic Sea Ice and the Winter NAO
urls.append('https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019GL083059')
# England 2019, Arctic internal variability sea ice. JClim
urls.append('https://journals.ametsoc.org/doi/full/10.1175/JCLI-D-18-0864.1')
# Ed BW 2019, Tropical and Midlatitude Impact on Seasonal Polar Predictability in the CESM
urls.append('https://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-19-0088.1')
# Bushuk 2017, Summer Enhancement of Arctic Sea Ice Volume Anomalies in the September-Ice Zone
urls.append('https://journals.ametsoc.org/doi/10.1175/JCLI-D-16-0470.1')
# Huang 2019, Thicker Clouds and Accelerated Arctic Sea Ice Decline: The Atmosphere‐Sea Ice Interactions in Spring
urls.append('https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019GL082791')
# Li, Zhang, Stuecker 2019, Different Effects of Two ENSO Types on Arctic Surface Temperature in Boreal Winter
urls.append('https://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-18-0761.1')
# Ogi 2016, Importance of combined winter and summer AO on September sea ice extent
urls.append('https://iopscience.iop.org/article/10.1088/1748-9326/11/3/034019/pdf')
# Park 2018, Dynamic and Thermodynamic Impacts of the Winter AO on Summer Sea Ice Extent
urls.append('https://journals.ametsoc.org/doi/pdf/10.1175/JCLI-D-17-0067.1')
#
#urls.append('')
#
#urls.append('')

###### Open URLS #######
for url in urls: 
    webbrowser.open(url, new=1)

print('Done')