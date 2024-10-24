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
    Svg: require("@site/static/img/existsxpx.svg").default,
    description: (
      <>
        Machine learning for formal verification and formal verification for
        machine learning
      </>
    ),
  },
  {
    title: "The beautiful Lighthaven campus",
    Svg: require("@site/static/img/lightcone.svg").default,
    description: (
      <>
        We welcome you to{" "}
        <a href="https://lighthaven.space">Lighthaven's campus</a>, onsite
        <a href="https://www.havenbookings.space/events/eternal-september">
          accommodations
        </a>{" "}
        available.
      </>
    ),
  },
  {
    title: "Make sure you register",
    Svg: require("@site/static/img/forallxpx.svg").default,
    description: (
      <>
        <a href="https://forms.gle/YU6eXCRKofFGiLKfA">Registration form here</a>
        . Please await confirmation email
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
