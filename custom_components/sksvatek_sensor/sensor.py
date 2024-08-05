"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from datetime import timedelta, datetime, date

MIN_TIME_BETWEEN_SCANS = timedelta(seconds=3600)

seznam = [[""],
        ["", "Nový rok", "Karina / Alexandra", "Daniela", "Drahoslav", "Andrea", "Traja králi / Antónia", "Bohuslava", "Severín", "Alexej", "Dáša", "Malvína", "Ernest", "Rastislav", "Radovan", "Dobroslava / Dobroslav", "Kristína", "Nataša", "Bohdana", "Mário", "Dalibor / Sebastián", "Vincent", "Zora", "Miloš", "Timotej", "Gejza", "Tamara", "Bohuš", "Alfonz", "Gašpar", "Ema", "Emil"],
        ["", "Tatiana", "Erika / Erik", "Blažej", "Veronika", "Agáta", "Dorota", "Vanda", "Zoja", "Zdenko", "Gabriela", "Dezider", "Perla", "Arpád", "Valentín", "Pravoslav", "Liana / Ida", "Miloslava", "Miloslava", "Jaromír", "Vlasta", "Lívia", "Eleonóra", "Etela", "Roman / Romana", "Matej / Mateo", "Frederik / Frederika", "Viktor", "Alexander", "Zlatica"],
        ["", "Albín", "Anežka", "Bohumil / Bohumila", "Kazimír", "Fridrich", "Radoslav / Radoslava", "Tomáš", "Alan / Alana", "Františka", "Bruno / Branislav", "Angela / Angelika", "Gregor" ,"Vlastimil" ,"Matilda" ,"Svetlana" ,"Boleslav" ,"Ľubica" ,"Eduard" ,"Jozef" ,"Víťazoslav / Klaudius" ,"Blahoslav" ,"Beňadik" ,"Adrián" ,"Gabriel" ,"Marián" ,"Emanuel" ,"Alena" ,"Soňa" ,"Miroslav" ,"Vieroslava" ,"Benjamín"],
        ["", "Hugo" ,"Zita" ,"Richard" ,"Izidor" ,"Miroslava" ,"Irena" ,"Zoltán" ,"Albert" ,"Milena" ,"Igor" ,"Július" ,"Estera" ,"Aleš" ,"Justina" ,"Fedor" ,"Dana / Danica" ,"Rudolf / Rudolfa" ,"Valér" ,"Jela" ,"Marcel" ,"Ervín" ,"Slavomír" ,"Vojtech" ,"Juraj" ,"Marek" ,"Jaroslava" ,"Jaroslav" ,"Jarmila" ,"Lea" ,"Anastázia"],
        ["", "Sviatok práce" ,"Žigmund" ,"Galina / Timea" ,"Florián" ,"Lesia / Lesana" ,"Hermína" ,"Monika" ,"Ingrida / Deň víťazstva nad fašizmom" ,"Roland" ,"Viktória" ,"Blažena" ,"Pankrác" ,"Servác" ,"Bonifác" ,"Žofia / Sofia" ,"Svetozár" ,"Gizela" ,"Viola" ,"Gertrúda" ,"Bernard" ,"Zina" ,"Júlia / Juliana" ,"Želmíra" ,"Ela" ,"Urban / Vivien" ,"Dušan" ,"Iveta" ,"Viliam" ,"Vilma" ,"Ferdinand" ,"Petrana / Petronela"],
        ["", "Žaneta" ,"Xénia / Oxana" ,"Karolína" ,"Lenka" ,"Laura" ,"Norbert" ,"Róbert / Róberta" ,"Medard" ,"Stanislava" ,"Margaréta / Gréta" ,"Jesika" ,"Zlatko" ,"Anton" ,"Vasil" ,"Vít" ,"Blanka / Bianka" ,"Adolf" ,"Vratislav" ,"Alfréd" ,"Valéria" ,"Alojz" ,"Paulína" ,"Sidónia" ,"Ján" ,"Olívia / Tadeáš" ,"Adriána" ,"Ladislav / Ladislava" ,"Beáta" ,"Peter / Pavol / Petra" ,"Melánia"],
        ["", "Diana" ,"Berta" ,"Miloslav" ,"Prokop" ,"Cyril / Metod" ,"Patrik / Patrícia" ,"Oliver" ,"Ivan" ,"Lujza" ,"Amália" ,"Milota" ,"Nina" ,"Margita" ,"Kamil" ,"Henrich" ,"Drahomír / Drahomíra" ,"Bohuslav" ,"Kamila" ,"Dušana" ,"Iľja / Eliáš" ,"Daniel" ,"Magdaléna" ,"Oľga" ,"Vladimír" ,"Jakub / Timur" ,"Anna / Hana / Anita / Aneta" ,"Božena" ,"Krištof" ,"Marta" ,"Libuša" ,"Ignác"],
        ["", "Božidara" ,"Gustáv" ,"Jerguš" ,"Dominika / Dominik" ,"Hortenzia" ,"Jozefína" ,"Štefánia" ,"Oskar" ,"Ľubomíra" ,"Vavrinec" ,"Zuzana" ,"Darina" ,"Ľubomír" ,"Mojmír" ,"Marcela" ,"Leonard" ,"Milica" ,"Elena / Helena" ,"Lýdia" ,"Anabela / Liliana" ,"Jana" ,"Tichomír" ,"Filip" ,"Bartolomej" ,"Ľudovít" ,"Samuel" ,"Silvia" ,"Augustín" ,"Nikola / Nikolaj / Výročie SNP" ,"Ružena" ,"Nora"],
        ["", "Drahoslava / Deň Ústavy Slovenskej republiky" ,"Linda / Rebeka" ,"Belo" ,"Rozália" ,"Regina" ,"Alica" ,"Marianna" ,"Miriama" ,"Martina" ,"Oleg" ,"Bystrík" ,"Mária / Marlena" ,"Ctibor" ,"Ľudomil" ,"Jolana / Sedembolestná Panna Mária" ,"Ľudmila" ,"Olympia" ,"Eugénia" ,"Konštantín" ,"Ľuboslav / Ľuboslava" ,"Matúš" ,"Móric" ,"Zdenka" ,"Ľuboš / Ľubor" ,"Vladislav / Vladislava" ,"Edita" ,"Cyprián" ,"Václav" ,"Michal / Michaela" ,"Jarolím"],
        ["", "Arnold" ,"Levoslav" ,"Stela" ,"František" ,"Viera" ,"Natália" ,"Eliška" ,"Brigita" ,"Dionýz" ,"Slavomíra" ,"Valentína" ,"Maximilián" ,"Koloman" ,"Boris" ,"Terézia" ,"Vladimíra" ,"Hedviga" ,"Lukáš" ,"Kristián" ,"Vendelín" ,"Uršuľa" ,"Sergej" ,"Alojzia" ,"Kvetoslava" ,"Aurel" ,"Demeter" ,"Sabína" ,"Dobromila" ,"Klára" ,"Šimon / Simona" ,"Aurélia"],
        ["", "Denis / Denisa" ,"Pamiatka zosnulých" ,"Hubert" ,"Karol" ,"Imrich" ,"Renáta" ,"René" ,"Bohumír" ,"Teodor" ,"Tibor" ,"Martin / Maroš" ,"Svätopluk" ,"Stanislav" ,"Irma" ,"Leopold" ,"Agnesa" ,"Klaudia / Deň boja za slobodu a demokraciu" ,"Eugen" ,"Alžbeta" ,"Félix" ,"Elvíra" ,"Cecília" ,"Klement" ,"Emília" ,"Katarína" ,"Kornel" ,"Milan" ,"Henrieta" ,"Vratko" ,"Ondrej / Andrej"],
        ["", "Edmund" ,"Bibiána" ,"Oldrich" ,"Barbora / Barbara" ,"Oto" ,"Mikuláš" ,"Ambróz" ,"Marína" ,"Izabela" ,"Radúz" ,"Hilda" ,"Otília" ,"Lucia" ,"Branislava / Bronislava" ,"Ivica" ,"Albína" ,"Kornélia" ,"Sláva" ,"Judita" ,"Dagmara" ,"Bohdan" ,"Adela" ,"Nadežda" ,"Adam / Eva / Štedrý deň" ,"Prvý sviatok vianočný" ,"Štefan / Druhý sviatok vianočný" ,"Filoména" ,"Ivana / Ivona" ,"Milada" ,"Dávid" ,"Silvester"]]
        
def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    add_entities([SKSvatekSensor()])


class SKSvatekSensor(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Sviatok dnes"
    
    #@Throttle(MIN_TIME_BETWEEN_SCANS)
    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        ted = datetime.now()
        jmeno = seznam[int(ted.strftime("%m"))][int(ted.strftime("%d"))]
        self._attr_native_value = jmeno
