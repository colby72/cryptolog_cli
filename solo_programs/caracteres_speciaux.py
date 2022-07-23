# THis code is the property of Ramy Chmak
# ---------------------------------------

symbol_sp = {
	'"': '&quot;',
	'«': '&laquo;',
	'»': '&raquo;',
	'‹': '&lsaquo;',
	'›': '&rsaquo;',
	'“': '&ldquo;',
	'”': '&rdquo;',
	'„': '&bdquo;',
	'‘': '&lsquo;',
	'’': '&rsquo;',
	'‚': '&sbquo;',
	'…': '&hellip;',
	'¡': '&iexcl;',
	'¿': '&iquest;',
	'¨': '&uml;',
	'´': '&acute;',
	'ˆ': '&circ;',
	'˜': '&tilde;',
	'¸': '&cedil;',
	'·': '&middot;',
	'•': '&bull;',
	'¯': '&macr;',
	'‾': '&oline;',
	'–': '&ndash;',
	'—': '&mdash;',
	'¦': '&brvbar;',
	'§': '&sect;',
	'¶': '&para;',
	'©': '&copy;',
	'®': '&reg;',
	'™': '&trade;',
	'&': '&amp;',
	'◊': '&loz;',
	'♠': '&spades;',
	'♣': '&clubs;',
	'♥': '&hearts;',
	'♦': '&diams;',
	'←': '&larr;',
	'↑': '&uarr;',
	'→': '&rarr;',
	'↓': '&darr;',
	'↔': '&harr;',
	'⇒': '&rArr;',
	'⇔': '&hArr;',
	'↵': '&crarr;',
	'⇐': '&lArr;',
	'⇑': '&uArr;',
	'⇓': '&dArr;',
	'À': '&Agrave;', 'à': '&agrave;', #lettres
	'À': '&Aacute;', 'á': '&aacute;',
	'Â': '&Acirc;', 'â': '&acirc;',
	'Ã': '&Atilde;', 'ã': '&atilde',
	'Ä': '&Auml', 'ä': '&auml;',
	'Å': '&Aring;', 'å': '&aring;',
	'Æ': '&AElig;', 'æ': '&aelig;',
	'Ç': '&Ccedil;', 'ç': '&ccedil;',
	'É': '&Eacute;', 'é': '&eacute;',
	'È': '&Egrave;', 'è': '&egrave;',
	'Ê': '&Ecirc;', 'ê': '&ecirc;',
	'Ë': '&Euml;', 'ë': '&euml;',
	'Ì': '&Igrave', 'ì': '&igrave;',
	'Í': '&Iacute', 'í': '&iacute;',
	'Î': '&Icirc', 'î': '&icirc;',
	'Ï': '&Iuml', 'ï': '&iuml;',
	'Ñ': '&Ntildee;', 'ñ': '&ntilde;',
	'Ò': '&Ograve;', 'ò': '&ograve;',
	'Ó': '&Oacute;', 'ó': '&oacute;',
	'Ô': '&Ocirc;', 'ô': '&ocirc;',
	'Õ': '&Otilde;', 'õ': '&otilde;',
	'Ö': '&Ouml;', 'ö': '&ouml;',
	'Ø': '&Oslash;', 'ø': '&oslash;',
	'Œ': '&OElig;', 'œ': '&oelig;',
	'Š': '&Scaron;', 'š': '&scaron;',
	'ß': '&szlig;',
	'Ð': '&ETH;', 'ð': '&eth;',
	'Þ': '&THORN;', 'þ': '&thorn;',
	'Ù': '&Ugrave', 'ù': '&ugrave;',
	'Ú': '&Ueacute;', 'ú': '&uacute;',
	'Û': '&Ucirc;', 'û': '&ucirc;',
	'Ü': '&Uuml;', 'ü': '&uuml;',
	'Ý': '&Yacute;', 'ý': '&yacute;',
	'Ÿ': '&Yuml;', 'ÿ': '&yuml;', #grec
	'Α': '&Alpha;', 'α': '&alpha;',
	'Β': '&Beta;', 'β': '&beta;',
	'Γ': '&Gamma;', 'γ': 'gamma;',
	'Δ': '&Delta;', 'δ': '&delta;',
	'Ε': '&Epsilon;', 'ε': '&epsilon;',
	'Ζ': '&Zeta;', 'ζ': '&zeta;',
	'Η': '&Eta;', 'η': '&eta;',
	'Θ': '&Theta;', 'θ': '&theta;',
	'Ι': '&Iota;', 'ι': '&iota;',
	'Κ': '&Kappa;', 'κ': '&kappa;',
	'Λ': '&Lambda;', 'λ': '&lambda;',
	'Μ': '&Mu;', 'µ': '&mu;',
	'Ν': '&Nu;', 'ν': '&nu;',
	'Ξ': '&Xi;', 'ξ': '&xi;',
	'Ο': '&Omicron;', 'ο': '&omicron;',
	'Π': '&Pi;', 'π': '&pi;',
	'Ρ': '&Rho;', 'ρ': '&rho;',
	'Σ': '&Sigma;', 'σ': '&sigma;', 'ς': '&sigmaf;',
	'Τ': '&Tau;', 'τ': '&tau;',
	'Υ': '&Upsilon;', 'υ': '&upsilon;',
	'Φ': '&Phi;', 'φ': '&phi;',
	'Χ': '&Chi;', 'χ': '&chi;',
	'Ψ': '&Psi;', 'ψ': '&psi;',
	'Ω': '&Omega;', 'ω': '&omega;',
	'¤': '&curren;', #devise
	'€': '&euro;',
	'¢': '&cent;',
	'£': '&pound;',
	'¥': '&yen;',
	'ƒ': '&fnof;',
	'°': '&deg;',
	'µ': '&micro;',
	'<': '&lt;',
	'>': '&gt;',
	'≤': '&le;',
	'≥': '&ge;',
	'≈': '&asymp;',
	'≠': '&ne;',
	'≡': '&equiv;',
	'±': '&plusmn;',
	'−': '&minus;',
	'×': '&times;',
	'÷': '&divide;',
	'⁄': '&frasl;',
	'‰': '&permil;',
	'¼': '&frac14;',
	'½': '&frac12;',
	'¾': '&frac34;',
	'′': '&prime;',
	'″': '&Prime;',
	'∂': '&part;',
	'∏': '&prod;',
	'∑': '&sum;',
	'√': '&radic;',
	'∞': '&infin;',
	'¬': '&not;',
	'∩': '&cap;',
	'∫': '&int;',
	'∀': '&forall;',
	'∃': '&exist;',	
	'∇': '&nabla;',
	'∈': '&isin;',
	'∋': '&ni;',
	'∝': '&prop;',
	'∠': '&ang;',
	'∧': '&and;',
	'∨': '&or;',
	'∪': '&cup;',
	'∴': '&there4;',
	'∼': '&sim;',
	'⊂': '&sub;',
	'⊃': '&sup;',
	'⊆': '&sube;',
	'⊇': '&supe;',
	'⊥': '&perp;',
	'⊕': '&oplus;',
	'℘': '&weierp;',
	'ℑ': '&image;',
	'ℜ': '&real;',
	'∅': '&empty;',
	'∉': '&notin;',
	'∗': '&lowast;',
	'≅': '&cong;',
	'⊄': '&nsub;',
	'⊗': '&otimes;',
	'ℵ': '&alefsym;',
	'ϑ': '&thetasym;',
	'ϖ': '&piv;',
	'ϒ': '&upsih;'
}
def conv_caractocode(carin):
	n = 0
	for car, code in symbol_sp.items():
		if car == carin:
			codout = code
			break
		n += 1
	if n == 0:
		print("Caractère introuvable dans le tableur ...")
	return codout
def conv_codetocarac(symbin):
	n = 0
	for car, symb in symbol_sp.items():
		if symb == symbin:
			carout = car
			break
		n += 1
	if n == 0:
		print("Code intouvable dans le tableur ...")
	return carout
print("Ceci est un tableur de caractères spéciaux")
print("------------------------------------------\n")
print("1- Caractère ==> Code")
print("2- Code ==> Caractère")
choice = 'a'
while choice != '1' and choice != '2':
	choice = input("\nChoisissez le programme adhéquoit à votre besoin : ")
if choice == '1':
	textin = input("Tapez le caractère : ")
	codeout = conv_caractocode(textin)
	print("Code : {}".format(codeout))
elif choice == '2':
	codein = input("Tapez le code : ")
	textout = conv_codetocarac(codein)
	print("Caractère : {}".format(textout))
