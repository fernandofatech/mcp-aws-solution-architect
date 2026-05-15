import Hero from "@/components/Hero";
import Features from "@/components/Features";
import Tools from "@/components/Tools";
import Quickstart from "@/components/Quickstart";
import Architecture from "@/components/Architecture";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <main className="min-h-screen">
      <Hero />
      <Features />
      <Tools />
      <Quickstart />
      <Architecture />
      <Footer />
    </main>
  );
}
