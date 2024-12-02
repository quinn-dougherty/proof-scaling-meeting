import clsx from "clsx";
import Heading from "@theme/Heading";
import styles from "./styles.module.css";

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<"svg">>;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: "ML4FV and FV4ML",
    Svg: require("@site/static/img/existential-quantifier.svg").default,
    description: (
      <>
        Machine learning for formal verification and formal verification for
        machine learning. Bringing leading practitioners and academics together
        to discuss ML to scale and automate formal methods will inspire new
        ideas and help clarify some of the bigger picture opportunities and
        applications
      </>
    ),
  },
  {
    title: "The beautiful Lighthaven campus",
    Svg: require("@site/static/img/lightcone.svg").default,
    description: (
      <>
        We welcome you to{" "}
        <a href="https://lighthaven.space">Lighthaven's campus</a>, onsite{" "}
        <a href="https://www.havenbookings.space/events/eternal-september">
          accommodations
        </a>{" "}
        available.
      </>
    ),
  },
  {
    title: "Make sure you register",
    Svg: require("@site/static/img/universal-quantifier.svg").default,
    description: <>Registration is closed</>,
  },
  {
    title: "Sponsored by Near AI",
    Svg: require("@site/static/img/near.svg").default,
    description: (
      <>
        Whether it's expertise, mindshare, adoption, developer experience, AI
        infrastructure, institutional support, funding, or the mission of
        supporting user-owned AI, <a href="https://near.org/ai">NEAR</a>{" "}
        Protocol is becoming the go-to choice for those building at the
        intersection of AI and Web3.
      </>
    ),
  },
  {
    title: "Sponsored by Beneficial AI Foundation",
    Svg: require("@site/static/img/baif.svg").default,
    description: (
      <>
        <a href="https://www.beneficialaifoundation.org">BAIF</a> supports a
        broad range of technical AI safety research though staff research,
        university partnerships and its Buterin Fellowship program.
      </>
    ),
  },
];

function Feature({ title, Svg, description }: FeatureItem) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
