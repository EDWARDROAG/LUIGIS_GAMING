import HeroBanner from '../components/HeroBanner'
import HeroCtaBand from '../components/HeroCtaBand'
import ShowcaseSection from '../components/ShowcaseSection'
import PromoSection from '../components/PromoSection'
import FeaturedGames from '../components/FeaturedGames'
import FeaturedConsoles from '../components/FeaturedConsoles'
import AccessoryGrid from '../components/AccessoryGrid'
import RepairServices from '../components/RepairServices'
import WaveDivider from '../components/WaveDivider'

export default function HomePage() {
  return (
    <>
      <HeroBanner />
      <HeroCtaBand />
      <ShowcaseSection />
      <WaveDivider />
      <section className="bg-pattern-gaming">
        <FeaturedGames />
      </section>
      <WaveDivider />
      <section className="bg-pattern-gaming">
        <FeaturedConsoles />
      </section>
      <WaveDivider />
      <section className="bg-pattern-gaming">
        <RepairServices />
      </section>
      <PromoSection />
      <WaveDivider />
      <section className="bg-pattern-gaming">
        <AccessoryGrid />
      </section>
      <WaveDivider />
    </>
  )
}
