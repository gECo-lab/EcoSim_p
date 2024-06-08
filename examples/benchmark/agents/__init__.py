# -*- coding: utf-8 -*-
"""
Agensts Model from the 
Basic Macroeconomic Model
Based on Caiani et al (2016)
"""

import datetime

from .agents import EconomicAgent
from .firm import Firm
from .cgfirm import CGFirm
from .kgfirm import KGFirm
from .bank import Bank
from .household import Household



__title__ = 'benchmark_model'
__version__ = '0.0.0'
__license__ = 'GPL-3.0'
__copyright__ = 'Copyright %s Ecos_p Team' % datetime.date.today().year


__all__ = ["EconomicAgent", "Household", "Firm", "CGFirm", "KGFirm", "Bank"]

